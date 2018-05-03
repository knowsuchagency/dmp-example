FROM python:3

WORKDIR /mysite

RUN pip install -U pip

COPY requirements.txt /mysite/

RUN pip install -r requirements.txt

COPY setup.py /mysite/

RUN pip install -e .
