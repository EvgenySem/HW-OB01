# Задача:
# Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task():
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status


def add_task(description, deadline):
    tasks.append(Task(description, deadline))


def mark_task(task):
    task.status = True
    print(f'Задача "{task.description}" выполнена')


def all_tasks():
    print('Список Ваших задач:')
    for task in tasks:
        if not task.status:
            print(f'{task.description}, срок выполнения: {task.deadline}')


tasks = []
add_task('To game', 'Till dayend')
add_task('To sleep', 'Till next day')
add_task('To eat', 'today')
add_task('To walk', 'whenever')

all_tasks()

mark_task(tasks[1])

all_tasks()
