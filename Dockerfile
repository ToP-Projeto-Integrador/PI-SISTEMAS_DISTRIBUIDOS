FROM python:3
ENV PYTHONNUNBUFFERED=1
WORKDIR /estagio
COPY requeriments.txt ./
RUN apt-get install libmariadb-dev-compat libmariadb-dev
RUN pip install -r requeriments.txt
COPY . /estagio