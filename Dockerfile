FROM python:3

WORKDIR /mysite

RUN pip install -U pip pipenv

COPY Pipfile* /mysite/

RUN pipenv install --system

COPY setup.py /mysite/

RUN pip install -e .
