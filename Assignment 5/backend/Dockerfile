FROM python:3.11-slim-buster

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt


WORKDIR /app
ADD . /app

ENTRYPOINT ["python"]
CMD ["app.py"]
