from time import sleep

from celery import shared_task


@shared_task
def check_depug():
    sleep(10)
    print("Check Depug")
    return True
