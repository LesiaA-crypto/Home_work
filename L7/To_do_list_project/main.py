import datetime
import show_tasks_module
import enter_task_module



def main():
    """Основная функция.
    Пользователь будет передавать значения для взаимодействия с программой."""

    # Выводим окно с условиями.
    show_tasks_module.cond_diplay()
    # Пустой список, в который будут добавляться все задачи пользователя.
    task_list = []
    cond_number = int(input("Выберите номер операции:"))

    while cond_number != 0:
        if cond_number == 1:
            try:
                enter_task_module.enter_task(task_list)
            except:
                print("Что-то пошло не так!")
        elif cond_number ==2:
            show_tasks_module.disp_task(task_list)
        elif cond_number ==3:
            show_tasks_module.cond_diplay()
        else:
            print("Не понимаю, выбери операцию")

        cond_number = int(input("Выберите номер операции:"))


if __name__ == "__main__":
    print("main.py запущен, как самостоятельный модуль (программа).")
    # Фиксируем начало работы с программой.
    starttime = datetime.datetime.now()
    main()
    # Фиксируем время выхода из программы.
    endtime = datetime.datetime.now()
    # Выводим пользователю количество потраченного времени в программе.
    print(f"Пока! Ты потратил {endtime - starttime}")
else:
    print("main.py запущен, как встроенный модуль (программа) в другую программу.")

