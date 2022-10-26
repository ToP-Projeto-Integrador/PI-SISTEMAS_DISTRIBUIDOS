FROM python:3
ENV PYTHONNUNBUFFERED=1
WORKDIR /estagio
COPY requeriments.txt ./
RUN pip install -r requeriments.txt
COPY . /estagio
