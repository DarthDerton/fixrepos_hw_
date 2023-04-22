"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


"""
The instances_counter decorator takes a cls class and returns a new NewClass class that inherits from cls.
Two methods are added to NewClass: get_created_instances and reset_instances_counter.

The __new__ method is overridden so that when a new instance of the cls class is created,
the created_instances counter is incremented.

The get_created_instances method returns the number of created instances of the cls class.

The reset_instances_counter method resets the created_instances counter and returns its reset value.
"""


def instances_counter(cls):
    class NewClass(cls):
        created_instances = 0

        def __new__(cls, *args, **kwargs):
            instance = super().__new__(cls)
            cls.created_instances += 1
            return instance

        @classmethod
        def get_created_instances(cls):
            return cls.created_instances

        @classmethod
        def reset_instances_counter(cls):
            count = cls.created_instances
            cls.created_instances = 0
            return count

    return NewClass


class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3