import csv

# Функция для проверки содержимого CSV файла
def check_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            if header != ['track_name', 'artist_name']:
                print("Некорректный заголовок файла CSV. Ожидается ['track_name', 'artist_name']")
                return

            print("Содержимое файла CSV:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")

# Проверьте файл playlist.csv
check_csv('playlist.csv')
