#!/usr/bin/env python3

import click
import sentry_sdk
from module.todos import Todo, TodoList, TodoFilter
from module.utils import parse_date


@click.group()
def cli():
    sentry_sdk.init(
        dsn="https://820bf9f2ce0bfac357be653ff1b567b8@o26192.ingest.us.sentry.io/4509010750210048",
        # Add data like request headers and IP for users,
        # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
        send_default_pii=True,
    )
    """Todo List CLI"""


LIST = TodoList()


@cli.command()
@click.argument("title")
@click.option("--description", "-d", default="", help="Todo description")
@click.option("--deadline", help="Todo deadline (YYYY-MM-DD)")
def add(title: str, description: str, deadline: str | None):
    """Add a new todo"""
    todo = Todo(
        id=len(LIST.todos) + 1,
        title=title,
        description=description,
        completed=False,
        deadline=deadline,
        completed_at=None,
    )
    LIST.add(todo)
    click.echo(f"Added todo: {todo.title}")


@cli.command()
@click.option("--completed", is_flag=True, help="Show completed todos")
@click.option("--deadline", help="Filter by max deadline (YYYY-MM-DD)")
def list(completed: bool, deadline: str | None):
    """List todos"""
    filter = TodoFilter(completed=completed)
    todos = LIST.get_todos(filter)

    total_completed = sum(1 for todo in todos if todo.completed)

    click.echo(f"TODO [{total_completed}/{len(todos)}]")
    click.echo("-" * 50)

    for todo in todos:
        status = "✓" if todo.completed else " "
        deadline_str = (
            todo.deadline.strftime("%Y-%m-%d") if todo.deadline else "No deadline"
        )
        click.echo(f"[{status}] {todo.id}. {todo.title} (Due: {deadline_str})")
        if todo.description:
            click.echo(f"   {todo.description}")

    click.echo(f"(completed: {total_completed / len(todos) * 100}%)")


@cli.command()
@click.argument("id", type=int)
def delete(id: int):
    """Delete a todo"""
    todo_list = TodoList()
    todo_list.delete(id)
    logger.info(f"Deleted todo with id {id}")


if __name__ == "__main__":
    cli()
