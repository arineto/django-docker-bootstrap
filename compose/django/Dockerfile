FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.base.txt /requirements.base.txt
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt \
    && groupadd -r django \
    && useradd -r -g django django

COPY . /app
RUN chown -R django /app

COPY ./compose/django/gunicorn.sh /gunicorn.sh
COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh \
    && sed -i 's/\r//' /gunicorn.sh \
    && chmod +x /entrypoint.sh \
    && chown django /entrypoint.sh \
    && chmod +x /gunicorn.sh \
    && chown django /gunicorn.sh

WORKDIR /app

RUN mkdir -p /app/staticfiles
RUN chown -R django:django /app/staticfiles

RUN mkdir -p /app/media
RUN chown -R django:django /app/media

RUN mkdir -p /home/django
RUN chown -R django:django /home/django

VOLUME /app/media
VOLUME /app/staticfiles

ENTRYPOINT ["/entrypoint.sh"]