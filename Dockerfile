FROM python:3

WORKDIR /workdir

RUN pip install -U pip pipenv

COPY Pipfile* /workdir/

RUN pipenv install --system

COPY setup.py /workdir/

COPY mysite /workdir/mysite

RUN pip install -e .

CMD python mysite/manage.py runserver 0.0.0.0:8000
