from django.urls import path

from shop.views import DelayReportView, AgentAssignView, DelaySummaryView

urlpatterns = [
    path('delay/', DelayReportView.as_view()),

]
