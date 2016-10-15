import json

def load_data(file_name):

    with open(file_name, "r", encoding="utf-8") as file_name:
        return json.loads(file_name.read())


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

if __name__ == '__main__':

        filename = ''

        while not filename:
            try:
                filename = input('Введите полное название до json файла: ')
                pretty_print_json(load_data(filename))
            except FileNotFoundError:
                print('Данного файла не существует в директории с программой')
