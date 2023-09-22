from django.shortcuts import render, HttpResponse
import logging

from seminar_1_app.functions import *

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.info('connection complieted')
    return HttpResponse('Hello World!')


def two(request):
    if heads_and_tails():
        logger.info('Значение стороны: Орёл')
        return HttpResponse('Орёл')
    else:
        logger.info('Значение стороны: Решка')
        return HttpResponse('Решка')


def cube(request):
    response = random_cube()
    logger.info(f'Значение {response}')
    return HttpResponse(f'Значение стороны: {response}')


def digest(request):
    response = random_digit()
    logger.info(f'РАНДОМНОЕ ЧИСЛО: {response}')
    return HttpResponse(f'РАНДОМНОЕ ЧИСЛО: {response}')
