from random import randint


class Ticket:
    def __init__(self, route, departure_time, price, num_place):
        self.__id_ticket = randint(1000000, 9999999)
        self.__route = route
        self.__departure_time = departure_time
        self.__price = price
        self.__num_place = num_place
        self.__sale_status = True

    @property
    def route(self):
        return self.__route

    @property
    def departure_time(self):
        return self.__departure_time

    @property
    def price(self):
        return self.__price

    @property
    def num_place(self):
        return self.__num_place

    @property
    def sale_status(self):
        return self.__sale_status

    def change_sale_status(self):
        self.__sale_status = not self.__sale_status

    def __str__(self):
        return f'Номер места {self.__num_place} - {"Свободно" if self.__sale_status else "Занято"}'
