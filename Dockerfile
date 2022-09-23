FROM python:3.9

WORKDIR /home/

RUN echo "test32156"

RUN git clone https://github.com/catlejuyeon/please.git

WORKDIR /home/please/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=please.settings.deploy && python manage.py migrate --settings=please.settings.deploy && gunicorn please.wsgi --env DJANGO_SETTINGS_MODULE=please.settings.deploy --bind 0.0.0.0:8000"]