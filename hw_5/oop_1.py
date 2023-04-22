"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истело ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from typing import Optional


"""
The Homework class takes as input the text of the task and the number of days to complete, and stores these attributes
in the appropriate fields. The is_active method checks to see if the job has timed out and returns True if the job is
still active, False otherwise.

The Student class takes the student's last name and first name as input and stores them in the appropriate fields.
The do_homework method takes a Homework object and returns it if the job is still active, otherwise it prints 
"You are late" and returns None.

The Teacher class takes the last name and first name of the teacher as input and stores them in the appropriate fields.
The create_homework method takes a job text and a number of days to complete, and returns a Homework instance.
"""


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return datetime.datetime.now() <= self.created + self.deadline


class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


def do_homework(self, homework: Homework) -> Optional[Homework]:
    if homework.is_active():
        return homework
    else:
        print("You are late")
        return None


class Teacher:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


def create_homework(self, text: str, deadline: int) -> Homework:
    return Homework(text, deadline)
