from hw_4.user import User


class UserRepos:
    def __init__(self):
        self.__users_list = []

    @property
    def users_list(self):
        return self.__users_list

    def access_provide(self, login, password):
        for user in self.__users_list:
            if user.login == login:
                if user.password == password:
                    user.change_access()
                    return user

    def add_user(self, login, password, fullname, agent):
        self.__users_list.append(
            User(login, password, fullname, agent)
        )
