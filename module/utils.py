from datetime import datetime
from pathlib import Path

import click


def get_file_contents(file_path: Path) -> bytes:
    return file_path.read_bytes()


def parse_date(date_str: str | None) -> datetime | None:
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        click.echo("Invalid date format. Please use YYYY-MM-DD")
        return None
