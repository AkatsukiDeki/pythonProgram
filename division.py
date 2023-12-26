import csv
from datetime import datetime
from datetime import timedelta
import shutil
import os
import modules.add_functions as ef


def get_data_for_date(current_date: datetime, data_file:str):
    """Функция для получения данных за определенную дату

    Аргументы:
    - current_date (datetime): текущая дата
    - data_file (str): имя файла с данными

    Возвращает:
    - None
    """
    pass


class WeatherDataIterator:
    """Класс для итерации по данным погоды

        Аргументы:
        - start_date (datetime): начальная дата
        - end_date (datetime): конечная дата
        - data_file (str): имя файла с данными

        Возвращает:
        - None
        """

    def __init__(self, start_date: datetime, end_date: datetime, data_file: str):
        self.start_date = start_date
        self.end_date = end_date
        self.current_date = start_date
        self.data_file = data_file

    def __iter__(self):
        return self

    def __next__(self):
        # Проверяем, что текущая дата не больше конечной даты
        if self.current_date > self.end_date:
            raise StopIteration

        # Извлекаем данные для текущей даты
        data = get_data_for_date(self.current_date, self.data_file)

        # Увеличиваем текущую дату на один день
        self.current_date += timedelta(days=1)

        # Пропускаем даты, для которых нет данных
        while data is None and self.current_date <= self.end_date:
            data = get_data_for_date(self.current_date, self.data_file)
            self.current_date += timedelta(days=1)

        # Возвращаем кортеж с текущей датой и соответствующими данными
        return (self.current_date - timedelta(days=1), data)

def division_date_and_data(directory_path: str, file_path: str) -> None:
    """Splitting the main file into two files by date and by data
    Args:
      directory_path: the path to the working directory for the shift
    """
    path = os.getcwd()
    os.chdir(directory_path)
    data = ef.read_data(file_path)
    with open('X.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([i[0].split("-") for i in data])
    with open('Y.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([i[1:] for i in data])
    os.chdir(path)



def split_csv_by_weeks(input_file: str, num_files: int):
    """Функция для разделения csv-файла на отдельные файлы по неделям

       Аргументы:
       - input_file (str): имя входного csv-файла
       - num_files (int): количество выходных файлов

       Возвращает:
       - None
       """
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    data_file = 'weather_data.csv'

    weather_data_iter = WeatherDataIterator(start_date, end_date, data_file)
    # Читаем исходный csv файл
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Пропускаем заголовок

        # Создаем словарь для хранения данных по неделям
        weeks_data = {}

        # Обрабатываем каждую строку в csv файле
        for row in reader:
            date_str = row[0]
            data = row[1:]

            # Преобразуем строку с датой в объект datetime
            date = datetime.strptime(date_str, '%Y-%m-%d')

            # Определяем номер недели для данной даты
            week_number = date.isocalendar()[1]

            # Добавляем данные в соответствующую неделю в словаре
            if week_number in weeks_data:
                weeks_data[week_number].append((date, data))
            else:
                weeks_data[week_number] = [(date, data)]

    # Создаем отдельные файлы для каждой недели
    for week_number, data in weeks_data.items():
        start_date = data[0][0]
        end_date = data[-1][0]
        file_name = f"{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.csv"

        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

            for date, row_data in data:
                writer.writerow([date.strftime('%Y-%m-%d')] + row_data)


        print(f"Файл {file_name} успешно создан.")

        datasets= "C:\\Users\\andre\\PycharmProjects\\pythonProject\\pythonProject4\\pythonProgram\\datasets"  # Замените на реальный путь

        # Прохождение по всем файлам в текущем каталоге
        for file_name in os.listdir(os.curdir):
            # Проверка, является ли файл csv
            if file_name.endswith('.csv'):
                # Перемещение файл в целевую папку
                shutil.move(file_name, datasets)

if __name__ == '__main__':
    main()
