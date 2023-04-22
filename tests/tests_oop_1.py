import pytest
import datetime
from oop_1 import Homework, Student, Teacher


"""
In this test, we use the pytest.mark.parametrize decorator to pass multiple parameters to each test function.
Each parameter includes a tuple,
the values to test.

In the test_homework_is_active function, we test the is_active method of the Homework class to make sure it returns the
expected result depending on the value of the deadline parameter.

In the test_student_full_name function, we test that the first_name and last_name properties of the Student class are
correctly combined into a full name.

In the test_student_do_homework function, we test the do_homework method of the Student class to make sure it returns
None if the deadline has passed and returns a Homework object if the deadline has not yet arrived.

In the test_teacher_create_homework function, we test the create_homework method of the Teacher class to make sure
it creates a Homework object with the correct text and deadline property values.

"""


@pytest.mark.parametrize("text, deadline, expected_result", [
    ("Math homework", 5, True),
    ("English homework", -1, False),
    ("Science homework", 0, False),
])
def test_homework_is_active(text, deadline, expected_result):
    homework = Homework(text, deadline)
    assert homework.is_active() == expected_result


@pytest.mark.parametrize("last_name, first_name, expected_result", [
    ("Doe", "John", "John Doe"),
    ("Smith", "Jane", "Jane Smith"),
])
def test_student_full_name(last_name, first_name, expected_result):
    student = Student(last_name, first_name)
    assert student.first_name + " " + student.last_name == expected_result


def test_student_do_homework():
    student = Student("Doe", "John")
    homework = Homework("Math homework", 5)
    assert student.do_homework(homework) == homework
    homework = Homework("English homework", -1)
    assert student.do_homework(homework) == None


@pytest.mark.parametrize("last_name, first_name, text, deadline", [
    ("Doe", "John", "Math homework", 5),
    ("Smith", "Jane", "English homework", -1),
])
def test_teacher_create_homework(last_name, first_name, text, deadline):
    teacher = Teacher(last_name, first_name)
    homework = teacher.create_homework(text, deadline)
    assert homework.text == text
    assert homework.deadline == datetime.timedelta(days=deadline)