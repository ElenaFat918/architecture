from abc import ABC, abstractmethod


class Drive(ABC):
    @abstractmethod
    def speed(self):
        pass

    @abstractmethod
    def stopped(self):
        pass


class SportDrive(Drive):
    def speed(self):
        print('разгон за 5 секунд')

    def stopped(self):
        print('остановка за 5 секунд')


class ClassicDrive(Drive):
    def speed(self):
        print('разгон за 10 секунд')

    def stopped(self):
        print('остановка за 10 секунд')
