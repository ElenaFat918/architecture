from hw_4.ticket import Ticket


class TicketRepos:
    def __init__(self, route, departure_time, price, count_places):
        self.__route = route
        self.__departure_time = departure_time
        self.__price = price
        self.__count_places = count_places
        self.__tickets_list = []

    def __str__(self):
        return f'маршрут: {self.__route}\n   время отправления {self.__departure_time} \n   стоимость:{self.__price}'

    def create_list_tickets(self):
        for num in range(1, self.__count_places + 1):
            self.__tickets_list.append(
                Ticket(self.__route, self.__departure_time, self.__price, num)
            )

    @property
    def tickets_list(self):
        return self.__tickets_list

    def sale(self, num_place):
        for ticket in self.__tickets_list:
            if ticket.num_place == num_place:
                if ticket.sale_status:
                    ticket.change_sale_status()

    @property
    def route(self):
        return self.__route

    def find_free_ticket(self, num):
        for ticket in self.__tickets_list:
            if ticket.num_place == num:
                if ticket.sale_status:
                    return ticket
