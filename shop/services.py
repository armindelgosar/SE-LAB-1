import abc
from datetime import datetime, timedelta

import pytz
import requests
from django.db.models.aggregates import Count
from shop.dataclasses import DelayServiceData, AgentServiceData
from shop.exceptions import DelayReportException, AgentAssignException
from shop.models import Order, DelayReport, DelayQueueItem, Agent
from shop.statics import TripStatus, DelayReportResult


class BaseService(abc.ABC):
    dataclass = None

    def validate_data(self, data):
        return self.dataclass(**data)

    @abc.abstractmethod
    def process(self, **kwargs):
        pass


class DelayReportService(BaseService):
    dataclass = DelayServiceData

    def get_new_delivery_duration(self):
        # result = requests.get('https://run.mocky.io/v3/122c2796-5df4-461c-ab75-87c1192b17f7').json()
        # return result['delivery_duration']
        return timedelta(seconds=10)

    def update_order_duration(self, order, user_name):
        delivery_duration = self.get_new_delivery_duration()
        order.delivery_duration = delivery_duration
        order.delivery_time = order.created + order.delivery_duration
        order.save()
        DelayReport.objects.create(name=user_name, trip=order.trip, result=DelayReportResult.DURATION_UPDATED, order=order)
        return {"result": f"delivery duration updated to {delivery_duration}"}

    def add_order_to_queue(self, order, user_name):
        if DelayQueueItem.objects.filter(order=order).exists():
            raise DelayReportException('order is already in delay queue')
        DelayQueueItem.objects.create(order=order)
        DelayReport.objects.create(name=user_name, result=DelayReportResult.ADDED_TO_DELAY_QUEUE, order=order)
        return {"result": "Added to delay queue"}

    def check_order_delivery_time(self, order):
        if order.delivery_time >= datetime.now(tz=pytz.UTC):
            raise DelayReportException('order is not delayed')

    def process(self, **kwargs):
        data = self.validate_data(kwargs)
        order_id = data.order_id
        user_name = data.name
        order = Order.objects.filter(id=order_id)
        if not order.exists():
            raise DelayReportException('order doesn\'t exist')
        order = order.first()
        self.check_order_delivery_time(order)
        if hasattr(order, 'trip') and order.trip.status in (TripStatus.PICKED, TripStatus.ASSIGNED, TripStatus.AT_VENDOR):
            return self.update_order_duration(order, user_name)
        return self.add_order_to_queue(order, user_name)


class AgentAssignService(BaseService):
    dataclass = AgentServiceData

    def get_order_from_queue(self):
        if DelayQueueItem.objects.count() == 0:
            raise AgentAssignException('queue is empty')
        queue_item = DelayQueueItem.objects.first()
        order = queue_item.order
        queue_item.delete()
        return order

    def process(self, **kwargs):
        data = self.validate_data(kwargs)
        agent_id = data.agent_id
        agent = Agent.objects.filter(id=agent_id)
        if not agent.exists():
            raise AgentAssignException('agent doesn\'t exist')
        agent = agent.first()
        if agent.order:
            raise AgentAssignException('agent is already assigned')
        order = self.get_order_from_queue()
        agent.order = order
        agent.save()
        return {'assigned_order_id': order.id}



