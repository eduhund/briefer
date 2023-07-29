import os
import random
from config import Config

def get_random_shot():
    file_list = os.listdir(Config.shots)
    random.seed()
    random_num = random.randrange(len(file_list))
    return file_list[random_num]

if __name__ == '__main__':
    print(get_random_shot())

