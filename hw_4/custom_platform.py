class CustomPlatform:
    def __init__(self, travel_repos, bank_rep):
        self.__user = None
        self.__bank_repos = bank_rep
        self.__travel_repos = travel_repos

    def registration(self, users, login, password, fullname, agent_travel):
        if self.__user is None:
            for user in users.users_list:
                if user.login == login:
                    return False
            users.add_user(login, password, fullname, agent_travel)
            self.__user = users.access_provide(login, password)
            return True
        return False

    def authorization(self, users, login, password):
        if self.__user is None:
            self.__user = users.access_provide(login, password)
            return True
        return False

    def logout(self):
        if self.__user is not None:
            self.__user.change_access()
            self.__user = None

    def edit_user(self):
        self.__user.full_name = input('введите новое ФИО: ')
        self.__user.card_bank = int(input('введите номер карты: '))

    def load_travels(self):
        return self.__travel_repos.travels

    def view_tickets(self, route):
        return self.__travel_repos.find_travel(route).tickets_list

    def buy_ticket(self, route, num, cvi):
        lst_tct = self.__travel_repos.find_travel(route)
        free_ticket = lst_tct.find_free_ticket(num)
        price = free_ticket.price
        if self.__bank_repos.buy_operation(self.__user.card_bank, cvi, price):
            free_ticket.change_sale_status()
            self.__user.tickets.append(free_ticket)

    def view_us_tickets(self):
        return self.__user.tickets

    def create_route(self, route, departure_time, price, count_places):
        self.__travel_repos.create_travel(self.__user.agent_travel, route, departure_time, price, count_places)
