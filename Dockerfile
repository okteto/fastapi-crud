FROM python:3.8

ADD requirements.txt /requirements.txt

ADD main.py /main.py

ADD okteto-pipeline.yaml /okteto-pipeline.yaml

ADD okteto-stack.yaml /okteto-stack.yaml

ADD okteto.yml /okteto.yml

RUN pip install -r requirements.txt

EXPOSE 8080

COPY ./app /app

CMD ["python3", "main.py"]