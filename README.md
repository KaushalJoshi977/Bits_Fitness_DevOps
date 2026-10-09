
# ACEest Fitness & Gym – DevOps Assignment 1

## About the Project

This project was developed as part of the Introduction to DevOps course at BITS Pilani.

The idea behind the assignment was to take a simple Python application and set up a basic DevOps workflow around it. This included managing the code through Git and GitHub, writing automated tests, running the application in Docker, and setting up CI pipelines using Jenkins and GitHub Actions.

For the application, I used Flask to create a small fitness and gym management service called ACEest Fitness & Gym.

The main focus of this assignment was not to build a complex fitness application, but to understand how different DevOps tools work together during software development and testing.

## Tools and Technologies

The following tools were used:

- **Python and Flask:** For developing the application.
- **Git and GitHub:** For version control and maintaining the repository.
- **Pytest:** For writing and running automated tests.
- **Docker:** For packaging and running the application in a container.
- **Jenkins:** For setting up a build and testing pipeline.
- **GitHub Actions:** For automatically validating code changes.
- **Ruff:** For basic Python code linting.
- **Gunicorn:** For serving the Flask application inside Docker.

## Application Overview

The Flask application provides information about three fitness programs:

1. Fat Loss
2. Muscle Gain
3. Beginner Fitness

Each program includes a workout recommendation and a basic diet plan.

The application also provides a health-check endpoint, which can be used to check whether the service is responding.

### Available Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Displays the application homepage |
| `/health` | Checks application health |
| `/api/programs` | Returns all fitness programs |
| `/api/programs/fat-loss` | Returns the Fat Loss program |
| `/api/programs/muscle-gain` | Returns the Muscle Gain program |
| `/api/programs/beginner` | Returns the Beginner program |

If an invalid fitness program is requested, the application returns a 404 response.

## Project Structure

```text
Bits_Fitness_DevOps/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── Jenkinsfile
├── README.md
│
├── tests/
│   └── test_app.py
│
└── .github/
    └── workflows/
        └── main.yml
```

## Running the Application Locally

The application can be run on a local machine using Python.

### 1. Clone the repository

```bash
git clone https://github.com/KaushalJoshi977/Bits_Fitness_DevOps.git
cd Bits_Fitness_DevOps
```

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
```

On Linux:

```bash
python3 -m venv .venv
```

### 3. Install dependencies

On Windows:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

On Linux:

```bash
.venv/bin/python -m pip install -r requirements.txt
```

### 4. Start the application

On Windows:

```powershell
.\.venv\Scripts\python.exe app.py
```

On Linux:

```bash
.venv/bin/python app.py
```

Once the server starts, open:

http://127.0.0.1:5000

The application should display the available fitness programs.

## Unit Testing with Pytest

I used Pytest to check whether the main parts of the application were working as expected.

The test cases cover:

- Homepage response
- Health-check endpoint
- Retrieving all fitness programs
- Retrieving each individual fitness program
- Handling an invalid program request
- Checking the fitness program data structure

To run the tests locally:

```bash
python -m pytest -v
```

If using the virtual environment, run Pytest through its Python executable instead.

### Test Result

A total of 8 tests were implemented, and all 8 passed successfully.

These tests were also executed inside Docker and through the Jenkins and GitHub Actions pipelines.

## Containerization Using Docker

The next part of the assignment was to containerize the application.

I created a Dockerfile using a Python 3.12 slim image. It installs the application dependencies and runs Flask through Gunicorn.

The container also runs using a non-root user.

### Build the Docker image

```bash
docker build -t aceest-fitness:1.0 .
```

### Run the container

```bash
docker run -d --name aceest-app -p 5000:5000 aceest-fitness:1.0
```

The application can then be accessed at:

http://localhost:5000

### Run tests inside Docker

```bash
docker run --rm --entrypoint python \
  aceest-fitness:1.0 \
  -m pytest -v -p no:cacheprovider
```

All 8 tests passed inside the Docker container.

Docker was tested on the BITS Pilani Prayogshala virtual machine.

This helped verify that the application works in a containerized environment and does not depend only on my local development setup.

## Jenkins Build Pipeline

For the Jenkins part of the assignment, I used the BITS Pilani Prayogshala VM.

Jenkins was configured to read the Jenkinsfile directly from the GitHub repository.

The pipeline has four main stages:

1. **Checkout Code:** Fetch the source code from GitHub.
2. **Setup Environment:** Create a Python virtual environment and install dependencies.
3. **Syntax Validation:** Check the Python files for syntax errors.
4. **Unit Testing:** Execute the Pytest test suite.

### Jenkins Configuration

- Job name: `ACEest-Fitness-BUILD`
- Job type: Pipeline
- SCM: Git
- Branch: `main`
- Script path: `Jenkinsfile`

### Jenkins Result

The Jenkins pipeline was executed successfully on the VM.

**Build #1: SUCCESS**

All 8 tests passed during the build.

This confirmed that Jenkins could fetch the project from GitHub, prepare the environment, and run the automated tests.

## CI Pipeline Using GitHub Actions

I also configured GitHub Actions to automatically run checks whenever code is pushed or a pull request is created.

The workflow file is located at:

`.github/workflows/main.yml`

The workflow performs the following steps:

1. Checkout the repository.
2. Set up Python 3.12.
3. Install the Ruff linting tool.
4. Check Python syntax.
5. Run Ruff linting.
6. Build the Docker image.
7. Execute Pytest inside the Docker container.

The workflow can also be started manually from the GitHub Actions tab.

### GitHub Actions Result

The workflow ran successfully after merging the GitHub Actions pull request.

All the required stages passed, including the Docker build and containerized tests.

The successful workflow can be viewed from the Actions tab of this repository.

## Git and GitHub Workflow

Git was used throughout the assignment to track changes and maintain different versions of the project.

Instead of making all changes directly on the main branch, I created separate branches for testing, Docker, Jenkins, and GitHub Actions.

Some of the branches used were:

- `feature/unit-tests`
- `feature/docker-container`
- `feature/jenkins-pipeline`
- `feature/github-actions-ci`

After completing each part, the changes were committed, pushed to GitHub, and merged through pull requests.

This made it easier to organize the work and track the progress of the assignment.

## Overall Results

| Task | Result |
|---|---|
| Flask application | Working |
| Git and GitHub setup | Completed |
| Pytest unit testing | 8 tests passed |
| Docker image build | Successful |
| Application running in Docker | Successful |
| Pytest inside Docker | 8 tests passed |
| Jenkins Build #1 | SUCCESS |
| GitHub Actions CI workflow | SUCCESS |

## What I Learned

This assignment helped me understand how the different parts of a DevOps workflow connect with each other.

Initially, I developed and tested the Flask application locally. After that, I moved the code to GitHub and used Docker to run it in a separate environment.

Setting up Jenkins gave me practical experience with creating a build pipeline, while GitHub Actions showed how testing and validation can happen automatically whenever changes are pushed to the repository.

One useful observation was that tests could run successfully inside Docker even when Pytest generated a cache-permission warning. Since the container runs as a non-root user, I used the `-p no:cacheprovider` option to avoid the warning during automated test execution.

Overall, the assignment provided hands-on experience with version control, containerization, automated testing, and continuous integration.

The project currently focuses on automated build and testing workflows. Deployment to a production server is not included.

## Repository

GitHub Repository:
https://github.com/KaushalJoshi977/Bits_Fitness_DevOps

**Course:** Introduction to DevOps  
**Institution:** BITS Pilani  
**Assignment:** 1  
**Project:** ACEest Fitness & Gym
