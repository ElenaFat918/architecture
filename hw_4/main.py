from hw_4.bank_repos import BankRepos
from hw_4.custom_platform import CustomPlatform
from hw_4.travel_repos import TravelRepos
from hw_4.user_repos import UserRepos

# Создадим пустой список пользователей
users = UserRepos()
# Создадим список -заглушку банка, добавляем список клиентов с данными карты
bank_rep = BankRepos()
bank_rep.create_new_client()
bank_rep.create_new_client()
bank_rep.create_new_client()
# Создадим пустой список направлений
travels = TravelRepos()

# Запуск теста CustomPlatform
# создадим CustomPlatform
custom = CustomPlatform(travels, bank_rep)
# регистрируем агента
custom.registration(users, input('login: '), input('password: '), input('FIO: '), True)
custom.logout()
# регистрируем пользователя
custom.registration(users, input('login: '), input('password: '), input('FIO: '), False)
custom.logout()
# авторизуем агента
custom.authorization(users, input('login: '), input('password: '))
# создаем маршрут направления
custom.create_route(input('Введите направление: '),
                    input('Введите дату отправления: '),
                    int(input('Введите стоимость билета: ')),
                    int(input('Введите количество мест: ')))
custom.logout()
# авторизуемся под пользователем
custom.authorization(users, input('login: '), input('password: '))
# редактируем пользователя, вводим карту
custom.edit_user()
# загружаем список направлений
print('------------load_travels------------__travels_list ')
for travel in custom.load_travels():
    print(travel)
# загружаем список билетов по направлению
print('------------view_tickets------------__tickets_list ')
for ticket in custom.view_tickets(input('Введите направление: ')):
    print(ticket)
# купим билет
print('------------buy_ticket------------__tickets_list ')
custom.buy_ticket(
    input('Введите направление: '),
    int(input('Введите номер места: ')),
    int(input('Введите cvi: '))
)
print('_____________user.tickets_________')
print(*custom.view_us_tickets())
print('------------view_tickets------------__tickets_list ')
for ticket in custom.view_tickets(input('Введите направление: ')):
    print(ticket)
