import abc


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(abc.ABC):

    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.hours = 8

    @abc.abstractmethod
    def calc_bonus(self):
        pass

    def get_hours(self):
        return self.hours


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_departament(self):
        return self._departament.name

    def set_department(self, departament_name):
        self._departament.name = departament_name


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self.__sales = 0

    def calc_bonus(self):
        return self.__sales * 0.15

    def get_sales(self):
        return self.__sales

    def put_sales(self, sales):
        self.__sales += sales
