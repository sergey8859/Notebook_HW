import csv
from datetime import date

file_name = "notes_name_01.csv"
timestamp = date.today()


def create_notes_file(file_name):
    notes_name = ['0', timestamp, 'Заметки   Note column']
    with open(file_name, 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        writer = writer.writerow(notes_name)

    with open(file_name, 'r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            return row


# Функция добавить новую заметку
def add_note():
    try:
        iD = input('Введите следующий порядковый номер заметки: ')
        timestamp = date.today()
        body = input('Введите текст заметки: ')
        row = [iD, timestamp, body]
    except ValueError:
        print("Ошибка при добавлении новой заметки")
    else:
        with open(file_name, 'a+', newline='', encoding='UTF-8') as file:
            writer = csv.writer(file)
            writer = writer.writerow(row)
            print("Заметка успешно создана!")
    return writer


# Создаем функцию для чтения заметок из файла
def read_notes_file():
    with open(file_name, 'r+', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
 #   return row


# Создаем функцию редактирования заметки
def exchange_note():

    iD = int(input('Введите цифру порядкового номера редактируемой заметки: '))
    new_body = input('Введите новый текст заметки: ')
    with open(file_name, 'r', encoding='UTF-8', newline='') as file:
        row = file.readlines()[iD]
        row = row.replace('Напомнить в среду день рождения у Коли! ', new_body)
        print(row)
    with open(file_name, 'a+', encoding='UTF-8', newline='') as file:
        file.write("".join(row))
    return row


# Создаем функцию поиска заметок по дате

def note_date():
    try:
        dates = input('Ведите дату для поиска заметки в виде: 2000-12-30: ')
    except ValueError:
        print("Ошибка при добавлении новой заметки")
    else:
        filtered_date = []
        with open(file_name, 'r', encoding='UTF-8', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == timestamp.strftime(dates):
                    filtered_date.append(row)
            print(filtered_date)


# Создаем функцию удаления заметки
def delete_note():
    iD = int(input('Введите цифру порядкового номера удаляемой заметки: '))
    with open(file_name, 'r', encoding='UTF-8', newline='') as inp:
        newrows = []
        data = csv.reader(inp)
        for row in data:
            if row[0] != iD:
                newrows.append(row)
        print(newrows)
    with open(file_name, 'w', encoding='UTF-8', newline='') as out:
        csv_writer = csv.writer(out)
        for row in newrows:
            csv_writer.writerow(row)


def main():
    while True:
        print('0. Создать файл для заметок (создается только один раз!)')
        print('1. Добавить новую заметку')
        print('2. Показать список заметок')
        print('3. Редактировать заметку')
        print('4. Выбрать заметку по дате')
        print('5. Удалить заметку')
        print('6. Выход из программы')
        try:
            choice = int(input('Введите цифру выбора действия: '))
        except ValueError:
            print('Ошибка ввода, попробуйте снова')
        else:
            if choice == 0:
                print(create_notes_file(file_name))
            if choice == 1:
                add_note()
            if choice == 2:
                read_notes_file()
            if choice == 3:
                exchange_note()
            if choice == 4:
                note_date()
            if choice == 5:
                delete_note()
            if choice == 6:
                print("До свидания!")
                break


if __name__ == '__main__':
    main()
