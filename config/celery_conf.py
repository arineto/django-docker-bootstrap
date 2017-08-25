#####################################
# CELERY
#####################################

from datetime import timedelta
from kombu import Exchange
from kombu import Queue


def celery_queue(key):
    return Queue(key, Exchange(key), routing_key=key)


CELERY_CREATE_MISSING_QUEUES = True
CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = (
    celery_queue('default'),
)


QUEUE_ROUTES = {
    'default': {'queue': 'default', 'routing_key': 'default'},
}


CELERY_RESULT_BACKEND = None

CELERY_TASK_SERIALIZER = 'json'

CELERY_ACCEPT_CONTENT = ['json']

CELERYD_MAX_TASKS_PER_CHILD = 1
