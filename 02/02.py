def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": int(age)
                    }
                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Некоректний формат даних у рядку: {line.strip()}")
                    continue
        return cats_info
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []
    except IOError:
        print("Помилка при читанні файлу.")
        return []

# Приклад використання функції
path_to_file = '02/02_cats_file.txt'
print(get_cats_info(path_to_file))