import modules.add_functions as ef


class DataIterator():
    """
    DataIterator - это класс, который итерирует по данным в заданном наборе данных.

    Аргументы:

    path (str): путь к файлу данных
    Атрибуты:

    __data (ndarray): массив данных
    __index (int): индекс текущего элемента итерации
    Методы:

    iter(self):
      Этот метод возвращает итератор для этого объекта DataIterator.
    next(self) -> tuple:
      Этот метод возвращает следующий элемент итерации в виде кортежа. Если все элементы были пройдены, вызывается исключение StopIteration.
    """


    def __init__(self, path: str):
        self.__data = ef.read_data(path)
        self.__index = -1

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value

    def __iter__(self):
        return self

    def __next__(self) -> tuple:
        if self.__index < len(self.__data) - 1:
            self.__index += 1
            return tuple(self.__data[self.__index])
        else:
            raise StopIteration