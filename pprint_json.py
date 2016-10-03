import json, os.path

def load_data(filepath):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = current_dir + '\\' + filepath
    file = open(data_file, "r", encoding="utf-8")

    return json.loads(file.read())


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':

        filename = ''

        while not os.path.isfile(filename):
            try:
                filename = input('Введите название json файла: ')
                pretty_print_json(load_data(filename))
            except FileNotFoundError:
                print('Данного файла не существует в директории с программой')