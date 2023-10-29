# Delivery delay handling system

The delay handling system is designed to monitor delay reports that occur while delivering products from vendors to customers.

It is developed using *Django* framework besides *sqlite* database.


### Development steps

1. Here is the project overview which has two main branches:
   `master`, and `main ` and we used the `feat/[FEATURE_NAME]` pattern to create feature branches.
<img width="1321" alt="Screen Shot 1402-08-07 at 16 26 57" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/161cee1c-2682-4ca1-a00b-36dceba2b832">
2. We've added a `.gitignore` file to ignore different directories like cache files and venv dir.
<img width="1093" alt="Screen Shot 1402-08-07 at 16 07 15" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/5d19f012-3e39-4c2a-888d-9dc7c201e2b5">
3. We generated some conflict scenarios to handle them using git cmd .e.g there were two branches for refactoring and reformatting and we had to merge them both in dev so there were some conflicts which we resolved and they're shown in screenshots below.
<img width="1241" alt="Screen Shot 1402-08-07 at 16 05 35" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/860297e9-536f-4375-b77d-8e3d109c534b">
<img width="1512" alt="Screen Shot 1402-08-07 at 16 00 43" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/fda6a664-29c4-4065-9d7a-13d4029a7070">
<img width="1512" alt="Screen Shot 1402-08-07 at 15 58 58" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/a544049a-92d9-4728-b184-5bff4d6962b7">
4. As a glance, here are some of our commands used for doing different stuff via git:
<img width="685" alt="Screen Shot 1402-08-07 at 15 55 31" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/5003dd18-13da-4279-8684-72f9a8a37bd5">
<img width="685" alt="Screen Shot 1402-08-07 at 15 57 26" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/b6f22d4d-e42a-4fc0-91ef-348a6a703a23">
5. We changed the default branch to `dev` and made the `master` protected branch.
<img width="1321" alt="Screen Shot 1402-08-07 at 16 10 38" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/63072483-26c4-4ea9-95a4-f1a8705059e2">
6. We created PR(pull request) in order to add different features to the main branches.
<img width="1093" alt="Screen Shot 1402-08-07 at 16 09 03" src="https://github.com/armindelgosar/SE-LAB-1/assets/60629485/620fb5ae-5b3e-4626-ae7c-da8d4ecfa5b2">


### Extra Questions
1. `.git` directory contains all config files which git needs regarding the project repository. Here we've mentioned some of them:
   - `head`: Keeping Track of Your Current Branch
   - `refs`: Storing References to Commits and Branches
   - `objects`: Storing Your Codebase as a Series of Snapshots
   - `config`: Storing Configuration Information for Git
   - `hooks`: Running Scripts at Specific Points in the Git Workflow
   - `hooks`: Running Scripts at Specific Points in the Git Workflow

2. `Atomic` in commit means all changes in a single commit should happen together. This means if one of the changes in a commit fails this causes all the commit fail. So we need to have an aggregated consistency. This principle is also works for each PR. PR is a group of commits in which all of its commits should be consistent and successful.
3. Here are the definitions and the differences:
   
`merge`: Merging creates a new commit that incorporates the changes from the specified branch into the current branch.

`rebase`: Rebase integrates the changes of one branch onto another, making the branch history linear and potentially avoiding unnecessary merge commits. So it doesn't have a commit for merging like `merge`

`cherry-pick`: Cherry-picking allows you to select specific commits and apply them onto the current branch, useful for picking individual changes without merging entire branches. So it is not working with branches, it is for cases when we need to work with an specific commit.

`fetch`: Fetch retrieves changes from a remote repository without merging them into your local branch. It updates your local knowledge of remote branches.

`pull`: Pull combines the fetch and merge steps, updating your local branch with changes from a remote branch with merge commit.
4. Here are the definitions and the differences:

`reset`: A powerful command that resets the working directory to a specific commit. Updates the current branch and the commit history as well.(It is recommended to use this command to undo uncommitted changes)

`revert`: Similar to `reset` though the only difference is that it creates a new commit for every revert operation.(It is recommended to use this command to undo committed changes)

`restore`: Restore files in the working tree from the index (the staging area where all git add-ed files reside) or another commit.(This command does not update your branch)
5. Git stage area is where you add the files(or changes) that you are going to commit. This allows you to choose which changed files you include in your commit.\

Git stash temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later on. Stashing is handy if you need to quickly switch context and work on something else, but you're mid-way through a code change and aren't quite ready to commit. You can restore these changes later with `git stash pop`.
6. A snapshot is the state of something (e.g. a folder) at a specific point in time. Each commit in git contains snapshot of the whole repository(instead of just saving changes)