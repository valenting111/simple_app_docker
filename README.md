# simple_app_docker

This project creates a simple web application using FastAPI, Uvicorn, Docker and Google Cloud Platform.
The idea is to explore the basic principles behind each of these technologies.

### FastAPI

FastAPI is a web framework for building APIs with Python (https://fastapi.tiangolo.com/) . 
In other words, it is a library that facilitates building APIs between an end user (Client) and a web server (Server).
Here the server side is implemented using Uvicorn (https://www.uvicorn.org/). 

### Recommended
I recommend to create a virtual environment for this simple project, to avoid any dependency issues with other projects. For that:
For MacOS and Linux:
```python3 -m pip install --user virtualenv```
For Windows:
```py -m pip install --user virtualenv```

Then:
For MacOS and Linux:
```python3 -m venv nameofenv```

For Windows:
```py -m venv nameofenv```

Activate the environment:

For MacOS and Linux:
```source env/bin/activate```

For Windows:
```.\env\Scripts\activate```

Install the dependencies required for this project:

```pip install -r requirements.txt```


### Deploying on localhost
First, you can check that the API works on your local computer before deploying it to the cloud.

In your terminal, navigate to this folder, activate your environment and run:
```uvicorn main:app --reload```

It should prompt a message telling you where the API is located on your personal computer.

### Dockerizing the app

To put this app in a container that can run on Google Cloud Platform, we write a Dockerfile that explains the steps necessary to build an image of this project and then run that image in a container. This can also be tested locally (make sure you have Docker installed and **running**):

```docker build -t myimagename .```

This builds the image of this project, assigns its name to ```myimagename```, using the current working directory ```.``` as context (meaning which folder should it refer to when handling files with relative paths for example). Then, you can run the container:

```docker run -d --name mycontainername myimagename```

This creates a container ```mycontainername``` from the ```myimagename``` image and runs it. This still all happens locally.

### Deploying on Google Cloud

Finally, to make the API available to anyone (with an internet connection), we deploy the docker container to Google Cloud Platform. There are multiple ways to do so: using Google Cloud Run, Google App Engine, Google Container Registry. Here we show how to use Google Cloud Run. Make sure you have a Google Cloud Platform account set up **with a billing account**. When you first sign up, GCP offers 300$ of free credits.

The concept is simple: Instead of building the docker image and running a container from it on our local computer, we ask Google to do it using the Google Cloud Console. This enables us to run commands in our terminal to interact with Google Cloud Platform.

The commands are:

- ```gcloud init``` : This command tells your computer to start connecting to Google Cloud. You will see multiple messages and questions:
- ```Pick configuration to use:``` Pick ```Re-initialize this configuration [default] with new settings```.
- ```Choose the account you would like to use to perform operations for this configuration:``` Choose your Google account that you linked to your Google Cloud Platform.

- ```Pick cloud project to use:``` Either pick a project your already created or create a new one (preferred option if you haven't used GCP before)

Now you need to tell GCP to build your image and run your container within the project you chose previously. Google often requires that you enable a lot of services for it to run something for you. While trying to build the image, it might warn you about this and offer to enable the required services. In this project, it seems that you need to enable:
- **service usage api**
- **cloud run api**
- **billing** (I think this cannot be enabled through the console, you need to do it on their website)

To build the image:

- ``` gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/CHOOSE_NAME_OF_YOUR_APP ``` 
For my particular case, sometimes I've had to run this command 2-3 times and enable every suggested service before it would finish successfully.

Once this is done, you can then ask GCP to run a container of this image using:

- ``` gcloud run deploy --image gcr.io/YOUR_PROJECT_ID/CHOOSE_NAME_OF_YOUR_APP ```

The prompt should then tell you where your app is available, and VOILA!



### request.py

This script is to do a simple test by pinging the different API endpoints of our app. You just need to substitute the url used with the url of your app.
