# Adler Viton Individual Project 4 [![CI/CD Pipeline](https://github.com/nogibjj/Av281_Individual_4/actions/workflows/actions.yml/badge.svg)](https://github.com/nogibjj/Av281_Individual_4/actions/workflows/actions.yml)
Auto Scaling Flask App Using Any Platform As a Service


FLASK APP LINK: https://sentimentanalysisapp.azurewebsites.net/

## Purpose
The purpose of this project was to build a publicly accessible auto-scaling container using Azure App Services and Flask. I wanted to build a publicly available sentiment analysis text analyzer. This allows a user to input any text, click analyze, and receive the sentiment label.

## Structure:


├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
├── .github/
│   └── workflows/
│       └── actions.yml
├── templates/
│   ├── input.html
│   └── sentiments.html
├── static/
│   └── css/
│       └── styles.css
├── Dockerfile
├── Makefile
├── README.md
├── flask_app.py
└── requirements.txt


## Important Aspects:

### CI/CD Pipeline:
This project also has a CI/CD pipeline, which is successfully running and consists of the following steps:
1. Setting up a Python environment
2. Installing project dependencies and packages
3. Formatting using Black formatter
4. Linting used Ruff

### HTML and CSS scripts: 
The two html files: [input.html](https://github.com/nogibjj/Av281_Individual_4/blob/main/templates/input.html) and [sentiments.html](https://github.com/nogibjj/Av281_Individual_4/blob/main/templates/sentiments.html) are the scripts that dictate how the user interface will work for the flask app. These are extremely simple examples of HTML files, with only a text insert box, button, and text display. The CSS file, [styles.css](https://github.com/nogibjj/Av281_Individual_4/blob/main/static/css/styles.css) is used for styling the HTML files. It has information about the colors, fonts, sizes, and so on of all the attributes used in the HTML files. 

### Flask
Flask is imported to create an app, using three main methods. First is the Flask(__name__) which turns the entire file into an app. Then, request and render_template are used to gather inputs from the user and render HTML templates within the app. 

### Dockerhub
Dockerhub is used to create and store a docker image of the whole Github repo. This essentially creates a containerization of the environment, flask_app.py, and associated UI files.

### Azure Web App
Azure Web App resource is used to deploy the docker image onto the public-facing URL. This is autoscaling for load handling through Azure.
