from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'QBuyPro.settings')

app = Celery('QBuyPro',
             broker='redis://:1qaz2wsx@47.102.218.113:6379/3', # 消息中间件存储的位置
             backend='redis://:1qaz2wsx@47.102.218.113:6379/4', # 结果存储的位置
             namespace='Celery')

app.config_from_object('django.conf.settings')
app.autodiscover_tasks()
