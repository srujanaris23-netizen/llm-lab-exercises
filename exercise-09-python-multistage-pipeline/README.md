# Exercise 9: Jenkins Multi-Stage Pipeline for a Python Flask Application

## 1. Aim

To create and execute a Jenkins Declarative Pipeline that automates the build, testing, code quality analysis, deployment, and application verification of a Python Flask application.

## 2. Objectives

- Automate dependency installation.
- Execute unit tests.
- Perform code quality checks.
- Deploy the application to a designated directory.
- Run and verify the deployed application.
- Understand multi-stage CI/CD pipeline execution.

## 3. Technologies Used

- Python
- Flask
- Git and GitHub
- Jenkins Declarative Pipeline
- Docker
- Python unittest
- Flake8

## 4. Application Description

The application is a simple Flask web application. When a client requests the root URL `/`, it returns the message:

`Hello, Jenkins Multi-Stage Pipeline!`

## 5. Pipeline Stages

1. **Build:** Install the application dependencies.
2. **Test:** Execute unit tests using Python's unittest framework.
3. **Code Quality:** Analyze the source files using Flake8.
4. **Deploy:** Copy the application files into the deployment directory.
5. **Run Application:** Start the Flask application in a Docker container.
6. **Test Application:** Send an HTTP request to verify the running application.

## 6. Testing

The unit test checks that:
- The root endpoint returns HTTP status code 200.
- The response body contains the expected message.

The application verification stage checks the HTTP response from the running application.

## 7. Expected Result

The pipeline should complete all stages successfully and display:

`Pipeline completed successfully!`

The final Jenkins build status should be `Finished: SUCCESS`.

Record the actual result after running the pipeline.

## 8. Screenshots

Add screenshots showing:
- The Jenkins pipeline configuration.
- The stages executing in Jenkins.
- Successful unit tests.
- The deployed application response.
- The final successful Console Output.

## 9. Conclusion

This exercise demonstrates how Jenkins can automate multiple steps of a Python application's CI/CD workflow through a Declarative Pipeline. It combines dependency installation, automated testing, code quality checks, deployment, and application verification into a repeatable process.
