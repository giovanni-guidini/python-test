from dataclasses import dataclass
from datetime import datetime
from typing import Self


@dataclass
class Todo:
    id: int
    title: str
    description: str
    completed: bool
    deadline: datetime | None
    completed_at: datetime | None

    def complete(self):
        self.completed = True
        self.completed_at = datetime.now()


@dataclass
class TodoFilter:
    completed: bool = False


class TodoList:
    todos: list[Todo]

    def __init__(self):
        self.todos = []

    def add(self, todo: Todo):
        self.todos.append(todo)

    def get_todos(self, filter: TodoFilter) -> list[Todo]:
        return [todo for todo in self.todos if todo.completed == filter.completed]

    def delete(self, todo_id: int):
        self.todos = [todo for todo in self.todos if todo.id != todo_id]

    def get_todo(self, todo_id: int) -> Todo:
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
