import data
import tasks_order

def test_get_order_by_track_status_200():
    response_track = tasks_order.new_order(data.order_body) #создание заказа
    track = response_track.json()['track']  #сохранение номера заказа
    response = tasks_order.get_order(track) #получение заказа по номеру
    assert response.status_code == 200