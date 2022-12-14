from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self, count):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):
        if self.get_free_space() >= count:
            if name in self.__items.keys():
                self.__items[name] += count
                return True
        else:
            print("На складе недостаточно места")
            return False

    def remove(self, name, count):
        if self.__items[name] >= count:
            self.__items[name] -= count
            return True
        else:
            print("На складе недостаточно места")
            return False

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

    def __str__(self):
        st = "\n"
        for key, value in self.__items.items():
           st += f"{key}:{value}\n"
        return st

class Shop(Store):
    def __int__(self, items, capacity=20):
        super().__init__(capacity)

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            print("Нельзя, слишком много уникальных товаров")
            return False
        else:
            super().add(name, count)

class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        action = req_list[0]
        self.__count = int(req_list[1])
        self.__item = req_list[2]
        if action == "Доставить":
            self.__from = req_list[4]
            self.__to = req_list[6]
        elif action == "Забрать":
            self.__from = req_list[4]
            self.__to = None
        elif action == "Привезти":
            self.__to = req_list[4]
            self.__from = None

    def move(self, storages):
        shop = Shop()
        storage = Storage()

        storages = {
            'магазин': shop,
            'склад': storage
        }

        to = storages.get(self.__to)
        from_som = storages.get(self.__from)
        if to.add(self.__item, self.__count):
                from_som.remove(self.__item, self.__count)
        elif self.to:
            to.add(self.__item, self.__count)
        elif from_som:
            from_som.remove(self.__item, self.__count)

        # if self.__to and self.__from:
        #     if eval(self.__to).add(self.__item, self.__count):
        #         eval(self.__from).remove(self.__item, self.__count)
        # elif self.__to:
        #     eval(self.__to).add(self.__item, self.__count)
        # elif self.__from:
        #     eval(self.__from).remove(self.__item, self.__count)


storage_1 =Store()
storage_2 =Store()
shop_1 =Shop(items={"Телефон":3, "Компютер":3, "Приставка":3})

while True:
    print("Текущие площади:")
    print(f"storage_1: {storage_1}")
    print(f"storage_2: {storage_2}")
    print(f"shop_1: {shop_1}")
    user_text = input("Введите команду:\n")
    if user_text == "стоп":
        break
    else:
        try:
           req = Request(user_text)
           req.move()
        except Exception as e:
            print(f"Произошла ошибка {e}")


# test_text = "Забрать 3 Телефон из shop_1"
# test_text_2 = "Доставить 1 Приставка из storage_1 в shop_1"
# req = Request(test_text_2)
# req.move()
# print(storage_1)
# print(shop_1)


# storage_1 = Shop(items={"Телефон":10, "Компютер":6})
#
# storage_1.add("Планшет", 6)
# storage_1.add("Приставка", 20)
# storage_1.add("Ноутбук", 50)
# storage_1.add("Наушники", 100)
# storage_1.add("Телевизор", 6)
#
#
# storage_1.remove("Телефон", 2)
# print(storage_1.get_free_space())
# print(storage_1.get_items())
# print(storage_1.get_unique_items_count())
#
# print(storage_1)
