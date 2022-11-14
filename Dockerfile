FROM python:3
ENV PYTHONNUNBUFFERED=1
WORKDIR /pisd
COPY . /pisd
RUN pip install -r requeriments.txt


