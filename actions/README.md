# Github actions


GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.



## Prereq
- Github repo 


## Simple setup and run (a _hello world_)

In a Github repo, add a workflows yaml file under the `.github/workflows` dir. This is the example from github:

```
name: GitHub Actions Demo
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v3
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```
Push the branch to remote (name of branch is not important). Navigate to the repo in `github.com` and check `actions`. There should be an execution. 

## What are the ins and outs of a workflow? 



### The workflow 

A workflow is a work package triggered by an _event_ in the repo. An event could be virtually anything that happens in the repo (open issue, close PR, ...). 

A repo can have none, one or many workflows. This makes it easier to keep track of and organise, but the workflows could also potentially reference each other. Maybe a workflow is needed when a PR is opened, and maybe a different workflow is needed when a push to a certain branch is done.


### The job

A workflow contains one or more _jobs_. A run is a work package that runs in a VM (or container), called a _runner_. So all things defined in a run will run in the same environment. This can be self hosted or hosted by GH. 


### The action 

A job contains a series of steps, that each define a piece of work (a script or an action -- a ready made extension that can be used.)

Actions can be GH defined, ready made ones, or can be defined in the actual repo or other repo, or as a registry image. 

#### Action based on script


#### GH ready made action




#### Custom actions (advanced use)

You can create actions by writing custom code that interacts with your repository in any way you'd like, including integrating with GitHub's APIs and any publicly available third-party API. For example, an action can publish npm modules, send SMS alerts when urgent issues are created, or deploy production-ready code.

If defined in same repo, it can be referenced in WF as: 
- uses: ./.github/actions/hello-world-action

if a yaml for the action is created in `./.github/actions/hello-world-action`. Ex:

```
name: "Example"
description: "Receives file and generates output"
inputs:
  file-path: # id of input
    description: "Path to test script"
    required: true
    default: "test-file.js"
outputs:
  results-file: # id of output
    description: "Path to results file"
```



## A workflow file 

```
name: <This would be the name of your WF>
on: [<When the WF will be triggered>] # this is a list or a scalar
jobs: # This is where you parallelize over multiple runners
  <Name of first job>:
    runs-on: <On what runner it should run>
    steps: # This is the sequential steps in the job (specified in list)
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event." # example of a script run
      - name: List files in the repository # example of using a name
        run: |
          ls ${{ github.workspace }}
      - name: Check out repository code # example of using a ready made GH action
        uses: actions/checkout@v3
      - run: echo "🍏 This job's status is ${{ job.status }}." # example of ref to internal job state
```


## Ready made workflows
https://github.com/actions/starter-workflows




## Thoughts 


The workflow is branch A is specified by the `.github/workflows/*` in branch A.

Actions can be found in repo page -> `actions`, or they are listed in PR. 


Actions can also be created in GUI, root page -> `actions` -> `new workflow`


Seems to be good to make a complex and repeatable task into an action. In this way, it it probable 
that it will save the most time.




# refs 

- [Github docs quickstart](https://docs.github.com/en/actions/quickstart)
- [Github learning docs](https://docs.github.com/en/actions/learn-github-actions)
- [Github custom actions](https://docs.github.com/en/actions/creating-actions)