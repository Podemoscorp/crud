FROM python:3.9

RUN adduser crud

WORKDIR /home/crud

RUN apt-get update -y
RUN apt-get install -y git gcc g++ tar libffi-dev 
RUN apt-get install -y python3-dev musl-dev postgresql

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt
RUN env/bin/pip install gunicorn pg8000

COPY api api
COPY user user
COPY crud crud
COPY static static
COPY templates templates
COPY core core
COPY manage.py ./

RUN chown -R crud:crud ./
USER crud

EXPOSE 8080
CMD env/bin/gunicorn --bind 0.0.0.0:8080 --access-logfile - --error-logfile - crud.wsgi