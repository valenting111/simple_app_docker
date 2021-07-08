FROM python:3.7-slim

#Copy our files such that the container knows which script to run
COPY . ./

#Install the necessary dependencies
RUN pip install -r requirements.txt

#Command to execute our container.
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app
