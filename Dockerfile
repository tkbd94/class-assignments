# Dockerfile -- Blueprint for building images
# Dockerimage -- Template for running containers
# Dockercontainer -- Running application with the packaged project

FROM python:3.10.4

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app .

#ADD main.py .

#RUN pip install pandas helpers

#ENV PYTHONPATH "${PYTHONPATH}:."

CMD [ "python", "./main.py" ]