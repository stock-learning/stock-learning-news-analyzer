FROM python:alpine3.7
COPY . /service-news-analyser
WORKDIR /service-news-analyser
RUN pip install -r requirements.txt
EXPOSE 6000