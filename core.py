# создание файла
import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# создание папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже есть')


# проверка наличия файла, функции
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# Удаление папки
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# Копирование файлов и папок
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print("Такая папка уже есть")
    else:
        shutil.copy(name, new_name)


# запись информации о работе менеджера в файл
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time}-{message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')



if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
    create_folder('new_f')
    create_folder('new_q')
    get_list()
    get_list(True)
    delete_file('new_q')
    copy_file('new_f', 'new_1')
    copy_file('text.dat', 'text_2.dat')
    save_info('12345')