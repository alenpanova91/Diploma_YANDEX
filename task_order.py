import configuration
import requests
import data

#создание заказа
def new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.header)

#получение заказа по номеру
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + str(track))