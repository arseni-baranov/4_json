import json

def load_data(file_name):

    with open(file_name, "r", encoding="utf-8") as file_name:
        return json.loads(file_name.read())


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

if __name__ == '__main__':

    def check_file_exists():
        try:
            filename = input('Введите полное название до json файла: ')
            pretty_print_json(load_data(filename))
        except FileNotFoundError:
            print('Данный файл не найден по указанному пути, попробуйте ещё раз')
            check_file_exists()
    
check_file_exists()
