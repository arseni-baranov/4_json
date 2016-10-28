import json


def load_data(file_name):

    with open(file_name, "r", encoding="utf-8") as file_name:
        return json.loads(file_name.read())


def format_json_data(data):
    return json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)


def main():
        try:
            filename = input('Введите полное название до json файла: ')
            print(format_json_data(load_data(filename)))
        except FileNotFoundError:
            print('Данный файл не найден по указанному пути')


if __name__ == '__main__':
    main()
