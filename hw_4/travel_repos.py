from hw_4.ticket_repos import TicketRepos


class TravelRepos:
    def __init__(self):
        self.__travels_list = []

    def create_travel(self, agent_status, route, departure_time, price, count_places):
        if agent_status:
            self.__travels_list.append(
                TicketRepos(route, departure_time, price, count_places)
            )
            self.__travels_list[-1].create_list_tickets()

    @property
    def travels(self):
        return self.__travels_list

    def find_travel(self, route):
        for travel in self.__travels_list:
            if travel.route == route:
                return travel
