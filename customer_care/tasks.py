from __future__ import absolute_import
from celery.decorators import task
from django.contrib.auth import get_user_model

__author__ = 'Otto'

@task()
def user_send_activation_email(user_id):
    user = get_user_model().objects.get(pk=user_id)
    user.send_activation_email()
