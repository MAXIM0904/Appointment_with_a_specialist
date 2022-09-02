from frontend import requests_to_the_server
from django.shortcuts import redirect

menu = {
    'user_out_logging': [
        {'title': 'Вход', 'url_name': 'home_page', 'method': 'GET'},
    ],

    'user_logging': [
        {'title': 'Добавить дни работы', 'url_name': '#', 'method': 'GET'},
        {'title': 'Выход', 'url_name': '#', 'method': 'GET'}
    ],

}


def token_update(request, dict_response, redirect_urls):
    """Функция обновляет токен и создает сессию для снижения количества запросов к серверу"""
    token_life = 60 * 60 * 24 * 10
    response = redirect(redirect_urls)
    response.set_cookie('token', dict_response['token'], max_age=token_life)
    return response


def token_control(request):
    if 'token' not in request.COOKIES:
        token = requests_to_the_server.urls_request(key_request='logging', payload=request.POST)
        token_update(request=request, dict_response=token, redirect_urls='/homepage/')
        return menu['user_out_logging']
    else:
        return menu['user_logging']
