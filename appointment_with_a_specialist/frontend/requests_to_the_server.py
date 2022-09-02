import requests
import json

base_urls = 'http://127.0.0.1:8000' #'http://dvdvdvgk.beget.tech'

requests_server = {
    'record':
        {'title': 'Запись к специалисту', 'urls': f"{base_urls}/record/all_record/", 'method': 'GET'},

    'user_record':
        {'title': 'Данные записи к специалисту', 'urls': f"{base_urls}/record/create_record/", 'method': 'POST'},

    'delete_record':
        {'title': 'Удаление записи к специалисту', 'urls': f"{base_urls}/record/delete/", 'method': 'DELETE'},

    'logging':
        {'title': 'Удаление записи к специалисту', 'urls': f"{base_urls}/api-token-auth/", 'method': 'POST'},

}


def urls_request(key_request, method=None, url=None, payload=None, headers=None, files=None):
    """ Общая функция направления запросов на сервер """
    if method is None:
        method = requests_server[key_request]['method']
    if url is None:
        url = requests_server[key_request]['urls']

    response = requests.request(method=method, url=url, headers=headers, data=payload, files=files)
    # print(response)
    # print(response.text)
    if response.status_code == 204:
        return True
    dict_response = json.loads(response.text)
    return dict_response