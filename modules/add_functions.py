import os
import csv
import datetime


def read_data(path: str) -> list:
    """
    Функция read_data считывает данные из файла CSV и возвращает список данных.

    Аргументы:

    path (str): путь к файлу данных
    Возвращает:

    data (list): список данных
    """

    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in csv.reader(file):
            data.append(line)
    return data


def growth(today: str, next_day: str) -> int:
    """
    Функция growth вычисляет количество дней роста между двумя датами.

    Аргументы:

    today (str): текущая дата в формате 'гггг-мм-дд'
    next_day (str): следующая дата в формате 'гггг-мм-дд'
    Возвращает:

    growth (int): количество дней роста
    """

    current_day = datetime.datetime.strptime(today, '%Y-%m-%d').date()
    following_day = datetime.datetime.strptime(next_day, '%Y-%m-%d').date()
    return (following_day - current_day).days