from django.shortcuts import render
from . import requests_to_the_server, utils
from django.shortcuts import redirect

def home_page(request):
    """ Домашняя страница """
    if request.method == "GET":
        payload = request.GET
        print('12345')
        print(payload)
        dict_response = requests_to_the_server.urls_request(key_request='record', payload=payload)
        return render(request, 'record_specialist/home_page.html', {'dict_response': dict_response})

    if request.method == "POST":
        return render(request, 'record_specialist/questionnaire.html', {'dict_response': request.POST})


def user_record(request):
    """ Страница анкеты для записи """
    if request.method == "POST":
        payload = request.POST
        dict_response = requests_to_the_server.urls_request(key_request='user_record', payload=payload)
        dict_response['message'] = dict_response
        return redirect('home_page')


def delete_pattern_record(request):
    """ Страница для ввода номера телефона для удаления """
    if request.method == "POST":
        return render(request, 'record_specialist/delete_record.html', {'dict_response': request.POST})


def delete_record(request):
    """ Удаление записи """
    if request.method == "POST":
        payload = request.POST
        requests_to_the_server.urls_request(key_request='delete_record', payload=payload)
        return redirect('home_page')


def logging(request):
    if request.method == "GET":
        return render(request, 'record_specialist/logging.html')

    if request.method == "POST":
        utils.token_control(request)
        return render(request, 'record_specialist/logging.html')
