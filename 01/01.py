def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    salaries.append(int(salary))
                except ValueError:
                    print(f"Некоректний формат даних у рядку: {line.strip()}")
                    continue
            
            total = sum(salaries)
            average = int(total / len(salaries)) if salaries else 0

            return f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0, 0
    except IOError:
        print("Помилка при читанні файлу.")
        return 0, 0

# Приклад використання функції
path_to_file = '01/01_salary_file.txt'
print(total_salary(path_to_file))