import task_class
import pytest


def test_add_lesson():
    """
    Тест для проверки добавления урока в расписании.
    """
    manager = task_class.LessonManager()  # Создаем новый менеджер
    manager.lesson_list = {}  # Очищаем список уроков перед тестом
    manager.add_lesson(1, "Google", "teacher1", "lesson1")
    assert 1 in manager.lesson_list


def test_find_lesson():
    """
    Тест для проверки поиска урока по ID в менеджере уроков.
    """
    manager = task_class.LessonManager()  # Создаем новый менеджер
    manager.lesson_list = {}  # Очищаем список уроков перед тестом
    manager.add_lesson(2, "Facebook", "teacher2", "lesson2")
    assert manager.find_lesson(2) is not None  # Ожидается, что метод вернет строку, а не None


def test_change_lesson():
    """
    Тест для проверки изменения урока по ID в менеджере уроков.
    """
    manager = task_class.LessonManager()  # Создаем новый менеджер
    manager.lesson_list = {}  # Очищаем список уроков перед тестом
    manager.add_lesson(3, "Twitter", "teacher3", "lesson3")
    manager.change_lesson(3, "Twitter", "teacher3", "new_lesson")
    assert manager.lesson_list[3][2] != "lesson3"  # Проверяем, что урок изменен


def test_duplicate_id():
    """
    Тест для проверки добавления записи с повторяющимся ID. Ожидается исключение ValueError.
    """
    manager = task_class.LessonManager()  # Создаем новый менеджер
    manager.lesson_list = {}  # Очищаем список уроков перед тестом
    manager.add_lesson(1, "Google", "teacher1", "lesson1")
    with pytest.raises(ValueError):
        manager.add_lesson(1, "Duplicate", "teacher2", "lesson2")
