import pandas as pd
import matplotlib.pyplot as plt


dataframe = pd.read_csv('datasets/dataset.csv')

dataframe.columns = ["Дата", "Температура по Цельсию", "Давление", "Направление", "Скорость"]
# Предполагая, что ваш DataFrame имеет 7 столбцов


def rename_columns(dataframe: pd.DataFrame, column_names: list) -> pd.DataFrame:
    """
    Переименовывает колонки DataFrame.

    Аргументы:
    dataframe (pd.DataFrame): Исходный DataFrame.
    column_names (list): Список новых имен колонок.

    Возвращает:
    pandas.DataFrame: DataFrame с переименованными колонками.
    """
    dataframe.columns = column_names
    return dataframe


def handle_invalid_values(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Обрабатывает невалидные значения в DataFrame.

    Аргументы:
    dataframe (pd.DataFrame): Исходный DataFrame.

    Возвращает:
    pandas.DataFrame: DataFrame с обработанными невалидными значениями.
    """
    return dataframe.fillna(method='ffill')


def add_fahrenheit_column(dataframe: pd.DataFrame, celsius_column: str) -> pd.DataFrame:
    """
    Добавляет столбец с температурой в шкале по Фаренгейту в DataFrame.

    Аргументы:
    dataframe (pd.DataFrame): Исходный DataFrame.
    celsius_column (str): Название столбца с температурой в Цельсиях.

    Возвращает:
    pandas.DataFrame: DataFrame с добавленным столбцом температуры в Фаренгейтах.
    """
    dataframe['Temperature_F'] = dataframe[celsius_column] * 9 / 5 + 32
    return dataframe


def compute_statistical_info(dataframe: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Вычисляет статистическую информацию для указанных столбцов в DataFrame.

    Аргументы:
    dataframe (pd.DataFrame): Исходный DataFrame.
    columns (list): Список названий столбцов для вычисления статистики.

    Возвращает:
    pandas.DataFrame: DataFrame с вычисленной статистической информацией.
    """
    return dataframe[columns].describe()


def filter_by_temperature(dataframe: pd.DataFrame, temperature: float) -> pd.DataFrame:
    """
    Фильтрует DataFrame по значению температуры.

    Аргументы:
    dataframe (pd.DataFrame): Исходный DataFrame.
    temperature (float): Значение температуры для фильтрации.

    Возвращает:
    pandas.DataFrame: Отфильтрованный DataFrame.
    """
    return dataframe[dataframe['Temperature'] == temperature]


def filter_by_date(dataframe: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Фильтрует DataFrame по дате.

    Аргументы:
    dataframe (pd.DataFrame): Исходный DataFrame.
    start_date (str): Начальная дата в формате 'гггг-мм-дд'.
    end_date (str): Конечная дата в формате 'гггг-мм-дд'.

    Возвращает:
    pandas.DataFrame: Отфильтрованный DataFrame.
    """
    return dataframe[(dataframe['Date'] >= start_date) & (dataframe['Date'] <= end_date)]


def group_by_month_and_compute_mean_temperature(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
        Вычисление среднемесячной температуры из DataFrame с группировкой по месяцам.

        Аргументы:
        dataframe (pd.DataFrame): Входной DataFrame.

        Возвращает:
        pd.DataFrame: Среднемесячная температура из DataFrame.
        """

    return dataframe.groupby(dataframe['Date'].dt.month)['Temperature', 'Temperature_F'].mean()

def plot_temperature_changes(dataframe: pd.DataFrame, date_column: str, temp_columns: list):
    """
    Построение графиков изменения температуры за весь период с использованием библиотеки matplotlib.

    Аргументы:
    dataframe (pd.DataFrame): Входной DataFrame.
    date_column (str): Название колонки с датой.
    temp_columns (list): Список названий колонок с температурой.

    Результат:
    График изменения температуры за весь период.
    """
    plt.figure(figsize=(10, 5))
    for column in temp_columns:
        plt.plot(dataframe[date_column], dataframe[column], label=column)
    plt.xlabel('Date')
    plt.ylabel('Temperature')
    plt.title('Temperature Changes')
    plt.legend()
    plt.show()
def show_monthly_temperature_statistics(dataframe: pd.DataFrame, month: int, year: int) -> None:
    """
    Отображение графика температуры за указанный месяц в году
    и отображение медианы и средних значений
    Аргументы:
      dataframe: DataFrame с исходными значениями
      month: Месяц, для которого строится график температуры
      year: Год, для которого строится график температуры
    """
    month_df = dataframe[(dataframe.Date.dt.month == month) & (dataframe.Date.dt.year == year)]
    fig = plt.figure(figsize=(30, 5))

    fig.add_subplot(1, 3, 1)
    plt.ylabel("Температура в Цельсиях")
    plt.xlabel("Дата")
    plt.plot(month_df.Date.dt.day, month_df["Температура в Цельсиях"],
             color='green', linestyle='-', linewidth=2, label='Температура в Цельсиях')
    plt.axhline(y=month_df["Температура в Цельсиях"].mean(), color='yellow', label="Среднее значение")
    plt.axhline(y=month_df["Температура в Цельсиях"].median(), color='blue', label="Медиана")
    plt.legend(loc=2, prop={'size': 10})

    fig.add_subplot(1, 3, 2)
    plt.ylabel("Температура в Фаренгейтах")
    plt.xlabel("Дата")
    plt.plot(month_df.Date.dt.day, month_df["Температура в Фаренгейтах"],
             color='red', linestyle='--', linewidth=2, label='Температура в Фаренгейтах')
    plt.axhline(y=month_df["Температура в Фаренгейтах"].mean(), color='yellow', label="Среднее значение")
    plt.axhline(y=month_df["Температура в Фаренгейтах"].median(), color='blue', label="Медиана")
    plt.legend(loc=2, prop={'size': 10})

    plt.show()

if __name__ == "__main__":
    filtered_temp_dataframe = filter_by_temperature(dataframe, 25)
    filtered_date_dataframe = filter_by_date(dataframe, '2023-01-01', '2023-12-31')
    show_monthly_temperature_statistics(filtered_date_dataframe, 1, 2023)
