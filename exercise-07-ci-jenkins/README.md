# Exercise 7: Continuous Integration Using Jenkins

## 1. Aim
To understand Continuous Integration (CI) and automate software testing using Jenkins.

## 2. Introduction
Continuous Integration is a software development practice in which code changes are integrated frequently and validated through automated builds and tests. Jenkins is an open-source automation server used to run jobs and pipelines.

## 3. Objectives
- Understand Continuous Integration.
- Learn Jenkins jobs, pipelines, stages, and builds.
- Automate Python unit testing.
- Examine build logs and results.

## 4. Tools and Technologies
- Windows 11
- Docker Desktop
- Jenkins
- Groovy / Jenkins Pipeline
- Python
- Git and GitHub
- Visual Studio Code

## 5. Key Concepts

### Continuous Integration
Frequently integrating code changes and validating them through automated processes.

### Jenkins
An automation server used to run jobs and pipelines.

### Pipeline
A sequence of automated steps defined for a task.

### Stage
A group of related pipeline steps, such as running tests.

### Build
One execution of a Jenkins job.

### Console Output
Logs that help identify errors and verify build results.

## 6. Procedure
1. Start Docker Desktop.
2. Start the Jenkins container.
3. Open Jenkins in a browser.
4. Open the Exercise-06-Monitoring job.
5. Click Build Now.
6. Open Console Output.
7. Record the actual build result.

## 7. Automated Testing
The monitoring exercise uses a Jenkins pipeline to run Python unit tests in a Docker container. The pipeline installs the dependencies and executes the tests.

## 8. Advantages
- Automates repetitive tasks.
- Executes tests consistently.
- Helps identify errors early.
- Maintains build history and logs.
- Supports integration with version control.

## 9. Security Considerations
- Protect Jenkins credentials.
- Restrict access to Jenkins.
- Keep Jenkins and plugins updated.
- Docker socket access grants significant control over the Docker host.
- Do not expose a development Jenkins server publicly without appropriate security controls.

## 10. Result
This exercise demonstrates Jenkins-based automation of software testing. Confirm the result using the actual Jenkins build status.

## 11. Screenshots
1. Jenkins dashboard.
2. Exercise-06-Monitoring job.
3. Build status.
4. Console Output showing test results.

Note: Report success only after verifying that Jenkins displays Finished: SUCCESS.
