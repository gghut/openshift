FROM daocloud.io/python:2-onbuild

RUN mkdir -p /app
WORKDIR /app

COPY ./* /app/

RUN pip install -r requirements.txt

CMD python controller.py