FROM python:3.8-buster

COPY requirements.txt /my_app/requirements.txt

RUN set -ex \
    && pip install --upgrade pip \
    && pip install -r my_app/requirements.txt --trusted-host pypi.python.org

WORKDIR /my_app
ADD . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "hr_bot.wsgi:application"]


