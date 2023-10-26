from random import randint


class User:
    def __init__(self, login, password, fullname, agent_travel):
        self.__uid = randint(1000000, 9999999)
        self.__login = login
        self.__password = password
        self.__fullname = fullname
        self.__card_bank = None
        self.__tickets = []
        self.__access = False
        self.__agent_travel = agent_travel

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_pass):
        if self.__access:
            self.__password = new_pass

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, new_fullname):
        if self.__access:
            self.__fullname = new_fullname

    @property
    def card_bank(self):
        return self.__card_bank

    @card_bank.setter
    def card_bank(self, new_data_bank):
        if self.__access:
            self.__card_bank = new_data_bank

    @property
    def access(self):
        return self.__access

    def change_access(self):
        self.__access = not self.__access

    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, ticket):
        if self.__access:
            self.__tickets.append(ticket)

    @property
    def agent_travel(self):
        return self.__agent_travel
