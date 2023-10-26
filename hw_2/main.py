from random import randint
from hw_2.diamond import DiamondGenerator
from hw_2.ferrum import FerrumGenerator
from hw_2.gem import GemGenerator
from hw_2.gold import GoldGenerator
from hw_2.leaky_sock import LeakySockGenerator


def diapasons(ch):
    if ch == 100:
        return 5
    elif 90 <= ch < 100:
        return 4
    elif 70 <= ch < 90:
        return 3
    elif 41 <= ch < 70:
        return 2
    else:
        return 1


for _ in range(25):
    chance = randint(1, 100)
    match diapasons(chance):
        case 1:
            reward = LeakySockGenerator()
            reward.open_reward()
        case 2:
            reward = FerrumGenerator()
            reward.open_reward()
        case 3:
            reward = GoldGenerator()
            reward.open_reward()
        case 4:
            reward = GemGenerator()
            reward.open_reward()
        case 5:
            reward = DiamondGenerator()
            reward.open_reward()
        case _:
            print('Упс, вы остались без награды')


