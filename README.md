# Report on CI/CD Pipeline Solution for Flask Application

## Components of the Solution:

- Flask Application:
  Flask is used to quickly create a web applications.
  It's serving as the web service to be deployed.
  It's the application that provides the endpoints and responds to HTTP requests.

- GitHub Actions:
  GitHub Actions is a crucial component of this solution.
  It's responsible for detecting code changes and running tests.
  Depending on these test results is determined
  whether or not the changes to the Flask app are deployed to a Linux server. In this case Digital Ocean VPS
  It does this by utilizing predefined workflows specified in YAML files.

- Digital Ocean:
  The Virtual Private Server (VPS) hosted on Digital Ocean is the target environment where the Flask application is deployed. It provides the infrastructure for running the application. Digital Ocean VPS offers scalability, reliability, and ease of deployment.

## Challenges Encountered and Solutions:

- Testing Environment: Setting up a testing environment in GitHub Actions required defining the correct Python version and installing project dependencies. The solution involved using the actions/setup-python action to set up Python 3.11.0 and installing required dependencies using pip install.

- SSH Key Configuration: One challenge was configuring SSH keys for secure communication between GitHub Actions and the VPS. The solution involved generating a new SSH key pair on the GitHub Actions runner, adding the public key to the VPS's authorized keys, and storing the private key as a GitHub secret.

- Deployment Process: Deploying the Flask application to the VPS required a well-defined script in the GitHub Actions workflow. The solution included creating a script that pulled the latest changes from the GitHub repository, restarted the service, and checked its status. Debugging was facilitated by using the debug: true option.
