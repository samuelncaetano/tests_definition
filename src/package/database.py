class Database:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def get_all(self):
        return self.__items

    def get(self, index):
        if 0 <= index < len(self.__items):
            return self.__items[index]
        return None
