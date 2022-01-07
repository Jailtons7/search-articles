FROM python:3.9-buster
ENV LANG pt-BR.utf8
ENV PYTHONUNBUFFERED=1
RUN mkdir /src
WORKDIR /src
RUN pip install --upgrade pip
COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /src/
