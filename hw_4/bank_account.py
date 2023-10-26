from random import randint


class BankAccount:
    def __init__(self, card, card_pass, balance):
        self.__id_client = randint(1000000, 9999999)
        self.__card = card
        self.__card_pass = card_pass
        self.__balance = balance

    @property
    def card(self):
        return self.__card

    @property
    def card_pass(self):
        return self.__card_pass

    @property
    def balance(self):
        return self.__balance

    def change_balance(self, price):
        if self.__balance > price:
            self.__balance -= price
            return True
        return False
