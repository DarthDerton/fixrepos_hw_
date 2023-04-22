import datetime
from collections import defaultdict
import pytest


"""
In this test, we use pytest.mark.parametrize to test the check_homework method of the Teacher class with multiple cases.
The decorator takes two arguments: a string representing the parameter name, and a list of tuples representing 
the parameter values and expected results. The test function takes two arguments:
the parameter value and the expected result.
The test function is run for each tuple in the list, and the results are aggregated and reported by pytest
"""


class DeadlineError(Exception):
    pass


class Person:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(days=deadline)
        self.created = datetime.datetime.now()

    def is_active(self):
        return datetime.datetime.now() < self.created + self.deadline


class Student(Person):
    def do_homework(self, homework, solution):
        if not homework.is_active():
            raise DeadlineError('You are late')
        return HomeworkResult(self, homework, solution)


class Teacher(Person):
    homework_done = defaultdict(set)

    @staticmethod
    def create_homework(text, deadline):
        return Homework(text, deadline)

    @classmethod
    def check_homework(cls, homework_result):
        if len(homework_result.solution) > 5:
            cls.homework_done[homework_result.homework].add(homework_result)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        if homework is None:
            cls.homework_done.clear()
        else:
            cls.homework_done.pop(homework, None)


class HomeworkResult:
    def __init__(self, author, homework, solution):
        if not isinstance(homework, Homework):
            raise TypeError('You gave a not Homework object')
        self.author = author
        self.homework = homework
        self.solution = solution
        self.created = datetime.datetime.now()


@pytest.mark.parametrize("solution, expected", [
    ("solution1", True),
    ("solution2", True),
    ("solution3", False),
    ("solution4", False),
])
def test_check_homework(solution, expected):
    teacher = Teacher("Doe", "John")
    homework = teacher.create_homework("Test homework", 5)
    student = Student("Smith", "Jane")
    homework_result = student.do_homework(homework, solution)
    assert teacher.check_homework(homework_result) == expected