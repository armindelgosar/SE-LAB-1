# Delivery delay handling system

The delay handling system is a system designed with aspect of monitoring delay reports occurred while delivering products from vendors to customers.

It is developed using *Django* framework besides *sqlite* database.


### Development steps

1. Here is the project overview which has two main branches:
   `master`, `main ` and we used `feat/[FEATURE_NAME]` pattern to create feature branches.
![overview pic](report_pics/Screen Shot 1402-08-07 at 16.26.57.png)
2. We've added a `.gitignore` file to ignore different directories like cache files and venv dir.
![overview pic](report_pics/Screen Shot 1402-08-07 at 16.07.15.png)
3. We generated some conflict scenarios to handle them using git cmd .e.g there was two branches for refactoring and reformatting which we had to merge them both in dev so there were some conflicts which we resolved and they're shown in screenshots below.
![overview pic](report_pics/Screen Shot 1402-08-07 at 16.05.35.png)
![overview pic](report_pics/Screen Shot 1402-08-07 at 16.00.43.png)
![overview pic](report_pics/Screen Shot 1402-08-07 at 15.58.58.png)
4. As a glance, here are some of our commands used for doing different stuff via git:
![overview pic](report_pics/Screen Shot 1402-08-07 at 15.55.31.png)
![overview pic](report_pics/Screen Shot 1402-08-07 at 15.57.26.png)
5. We changed the default branch to `dev` and made `master` protected branch.
![overview pic](report_pics/Screen Shot 1402-08-07 at 16.10.38.png)
6. We created PR(pull request) in order to add different features to main branches.
![overview pic](report_pics/Screen Shot 1402-08-07 at 16.09.03.png)
