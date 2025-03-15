class LessonManager:
    """Класс для управления записями уроков."""

    def __init__(self):
        self.lesson_list = {}

    def add_lesson(self, less_id, name, lastname, lesson):
        """Добавление записи урока с проверкой длины строк."""
        if less_id in self.lesson_list:
            raise ValueError("Урок с таким ID уже существует!")

        # Проверка на минимальную длину
        if len(name) < 3 or len(lastname) < 3 or len(lesson) < 3:
            raise ValueError("Название урока, Имя и Фамилия преподавателя должны быть длиной не менее 3 символов!")

        self.lesson_list[less_id] = (name, lastname, lesson)

    def find_lesson(self, less_id):
        """Поиск записи урока по ID."""
        if less_id in self.lesson_list:
            name, lastname, lesson = self.lesson_list[less_id]
            return f"Имя преподавателя: {name}, Фамилия преподавателя: {lastname}, Урок: {lesson}"
        else:
            print("Урок с таким ID не найден!")  # Сообщение, если урок не найден
            return None

    def change_lesson(self, less_id, new_name, new_lastname, new_lesson):
        """Изменение записи урока."""
        if less_id in self.lesson_list:
            self.lesson_list[less_id] = (new_name, new_lastname, new_lesson)
        else:
            print("ID не найден!")

    def delete_lesson(self, less_id):
        """Удаление записи урока по ID."""
        if less_id in self.lesson_list:
            del self.lesson_list[less_id]
            print(f"Урок с ID {less_id} был удален.")
        else:
            print("ID не найден!")

    def show_all_lessons(self):
        """Показать все записи уроков."""
        if self.lesson_list:
            for less_id, (name, lastname, lesson) in self.lesson_list.items():
                print(f"ID: {less_id}, Имя преподавателя: {name}, Фамилия преподавателя: {lastname}, Урок: {lesson}")
        else:
            print("Нет сохраненных уроков.")
