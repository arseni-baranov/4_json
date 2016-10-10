import json
import os.path


def load_data(file_name):
    current_dir = os.path.abspath(__file__)
    script_name = os.path.basename(__file__)

    data_file = current_dir.replace(script_name, '') + file_name

    with open(data_file, "r", encoding="utf-8") as data_file:
        return json.loads(data_file.read())


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

if __name__ == '__main__':

        filename = ''

        while not os.path.isfile(filename):
            try:
                filename = input('Введите название json файла: ')
                pretty_print_json(load_data(filename))
            except FileNotFoundError:
                print('Данного файла не существует в директории с программой')
