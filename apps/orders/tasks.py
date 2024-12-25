from celery import shared_task

@shared_task
def add():
    print('Hello Word')
    return 0
