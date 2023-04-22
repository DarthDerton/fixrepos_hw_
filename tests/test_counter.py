import pytest
from counter import instances_counter


"""
Функция test_get_created_instances проверяет,
что метод get_created_instances возвращает правильное количество созданных экземпляров класса User.

Функция test_reset_instances_counter использует декоратор pytest.mark.parametrize,
чтобы запустить несколько тестовых случаев с разными значениями для reset_count и expected_count.
В каждом тестовом случае мы создаем несколько экземпляров класса User,
затем вызываем метод reset_instances_counter несколько раз и проверяем, что он возвращает ожидаемое значение.
"""


@instances_counter
class User:
    pass


def test_get_created_instances():
    assert User.get_created_instances() == 0
    user1, user2, user3 = User(), User(), User()
    assert user1.get_created_instances() == 3


@pytest.mark.parametrize("reset_count, expected_count", [(0, 3), (1, 2), (2, 1), (3, 0)])
def test_reset_instances_counter(reset_count, expected_count):
    user1, user2, user3 = User(), User(), User()
    for i in range(reset_count):
        user1.reset_instances_counter()
    assert user1.reset_instances_counter() == expected_count