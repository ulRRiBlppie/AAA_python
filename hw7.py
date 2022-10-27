import json
import keyword


class Json_to_object():
    """
    Класс, который преобразует json  в объект, к атрибутам которого
    можно обращаться через точку
    """
    def __init__(self, data):
        if isinstance(data, str):
            data = json.loads(data)
        elif isinstance(data, dict):
            pass
        else:
            print('Error')

        for key, val in data.items():
            if keyword.iskeyword(key):
                key += '_'

            setattr(self, key, self.compute_attr_value(val))

    def compute_attr_value(self, value):
        if isinstance(value, list):
            return [self.compute_attr_value(x) for x in value]
        elif isinstance(value, dict):
            return Json_to_object(value)
        else:
            return value


class ColorizeMixin():
    """
    Миксин, который меняет цвет вывода, делает вывод согласно
    __repr__  следующего класса в очереди наследования,
    и возвращает цвет обратно
    """
    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m\
            {super().__repr__()} \033[1;0;40m'


class BaseAdvert(Json_to_object):
    """
    Класс, который
    1) инициализирует объект из json
    2) проверяет ограничения на price
    3) устанавливает вывод в нужном виде
    """

    def __init__(self, lesson_str):

        self.price = 0
        super().__init__(lesson_str)
        if self.price < 0:
            raise ValueError('price must be >= 0')

    def __repr__(self):
        return f' {self.title} | {self.price} ₽'


class Advert(ColorizeMixin, BaseAdvert):
    """
    Окончательный класс, который наследуют все характеристики
    классов-родителей
    """

    def __init__(self, lesson_str, repr_color_code=32):
        self.repr_color_code = repr_color_code
        super().__init__(lesson_str)


if __name__ == '__main__':
    lesson_str = """{

        "title": "python",
        "price": 10,
        "class": "korgi",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
    }"""
    # объект инициализируется из json
    advert_oblect = Advert(lesson_str, repr_color_code=32)
    # сам класс не содержит никаких атрибутов
    print(Advert.__dict__)
    # печатает надпись зеленым цветом
    print(advert_oblect)
    # можно обращаться к атрибутам через точку, в том числе к вложенным
    # К полю class можно обращаться по имени class_
    print(advert_oblect.price, advert_oblect.location.address,
          advert_oblect.class_)
    print(advert_oblect.__dict__)
