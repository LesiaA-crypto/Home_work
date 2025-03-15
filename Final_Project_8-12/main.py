import task_class


def menu():
    """
    Функция для отображения меню с доступными действиями пользователя.
    """
    print("""
         1 - добавить запись урока
         2 - просмотреть все уроки
         3 - найти урок по ID
         4 - изменить запись урока по ID
         5 - удалить запись урока по ID
         -1 - выйти из расписания уроков""")


def main():
    """
    Основная функция программы. Обрабатывает ввод пользователя, вызывает
    соответствующие методы для управления уроками, отображает меню и
    выполняет проверки на корректность ввода.
    """
    print("Привет! Это расписание уроков первоклассника!")
    manager = task_class.LessonManager()  # Создаем объект менеджера уроков
    menu()

    while True:
        try:
            oper = int(input("Выбери нужную функцию из меню: "))
            if oper < -1 or oper > 5:  # Проверка на корректность ввода
                print("Неверный выбор! Пожалуйста, выбери число от -1 до 5.")
                continue
            if oper == 0:  # Обработка случая, если введен 0
                print("Ошибка! Пункт с номером 0 отсутствует в меню.")
                continue
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите число.")
            continue

        if oper == -1:
            print("До свидания!")
            break  # Завершаем программу

        elif oper == 1:
            # Проверка ID
            while True:
                try:
                    less_id = int(input("Введите ID для записи: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            # Проверка обязательных полей
            while True:
                name = input("Введите Имя преподавателя: ").strip()
                if len(name) >= 3:
                    break
                print("Ошибка! Имя преподавателя должно быть не менее 3 символов.")

            while True:
                lastname = input("Введите фамилию преподавателя: ").strip()
                if len(lastname) >= 3:
                    break
                print("Ошибка! Фамилия должна быть не менее 3 символов.")

            while True:
                lesson = input("Введите урок: ").strip()
                if len(lesson) >= 3:
                    break
                print("Ошибка! Урок должен быть не менее 3 символов.")

            try:
                manager.add_lesson(less_id, name, lastname, lesson)  # Добавление урока
            except Exception as e:
                print(e)

        elif oper == 2:
            manager.show_all_lessons()  # Отображение всех уроков
        elif oper == 3:
            # Проверка ID
            while True:
                try:
                    less_id = int(input("Введите ID для поиска урока: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            result = manager.find_lesson(less_id)  # Поиск урока по ID
            if result:  # Если урок найден, вывести его
                print(result)

        elif oper == 4:
            # Проверка ID для изменения урока
            while True:
                try:
                    less_id = int(input("Введите ID для изменения урока: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")

            # Проверка обязательных полей
            while True:
                new_name = input("Введите новое имя преподавателя: ").strip()
                if new_name and len(new_name) >= 3:
                    break
                print("Ошибка! Имя  должно быть не менее 3 символов.")

            while True:
                new_lastname = input("Введите новую фамилию: ").strip()
                if new_lastname and len(new_lastname) >= 3:
                    break
                print("Ошибка! Фамилия должна быть не менее 3 символов.")

            while True:
                new_lesson = input("Введите новый урок: ").strip()
                if new_lesson and len(new_lesson) >= 3:
                    break
                print("Ошибка! Урок должен быть не менее 3 символов.")

            # Попытка изменить урок
            manager.change_lesson(less_id, new_name, new_lastname, new_lesson)  # Изменение урока

        elif oper == 5:
            # Проверка ID для удаления урока
            while True:
                try:
                    less_id = int(input("Введите ID для удаления урока: "))
                    break
                except ValueError:
                    print("Ошибка ввода ID! Пожалуйста, введите число.")
            manager.delete_lesson(less_id)  # Удаление урока

        menu()  # Выводим меню после выполнения действия


if __name__ == "__main__":
    main()  # Запуск основной функции
    