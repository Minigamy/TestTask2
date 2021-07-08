import random


def sorting(word):
    """Функция, которая преобразует слово в список и сортирует его."""
    word_list = sorted([x.lower() for x in word])
    return word_list


def mac_generator():
    """Функция, которая возвращает случайный мак адрес"""
    mac = [0x00, 0x24, 0x81,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff)]

    return ':'.join(map(lambda x: "%02x" % x, mac))


def random_type():
    """Функция возвращает случайный тип устройства"""
    type_list = ["emeter", "zigbee", "lora", "gsm"]
    random_num = random.randint(0, 3)
    return type_list[random_num]
