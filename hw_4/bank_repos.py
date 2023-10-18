from hw_4.bank_account import BankAccount


class BankRepos:
    def __init__(self):
        self.__clients_list = []

    def create_new_client(self):
        card = int(input('введите номер карты: '))
        card_pass = int(input('установите cvi-код: '))
        balance = int(input('введите баланc: '))
        self.__clients_list.append(BankAccount(card, card_pass, balance))

    def buy_operation(self, card, cvi, price):
        for client in self.__clients_list:
            if client.card == card:
                if client.card_pass == cvi:
                    return client.change_balance(price)
        return False
