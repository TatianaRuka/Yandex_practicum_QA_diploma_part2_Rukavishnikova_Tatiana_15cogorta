import requests
import configuration
import data

#создание нового заказа
def post_new_order():
    return requests.post(url=configuration.URL_SERVICE + configuration.ORDERS_PATH,
                         json=data.order_data,
                         headers=data.headers)

#получение заказа по номеру трека
def get_order_by_track(track):
    return requests.get(url=f"{configuration.URL_SERVICE}{configuration.ORDERS_PATH}/track?t={track}")
