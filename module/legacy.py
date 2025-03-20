import dotenv
import os


def get_greeting(locale: str) -> str | None:
    locales = {
        "en": "Hello",
        "fr": "Bonjour",
        "es": "Hola",
        "pt": "Olá",
    }
    return locales.get(locale)


def load_greeting() -> str | None:
    dotenv.load_dotenv()
    username = os.getenv("USERNAME")
    if not username:
        return None
    locale = os.getenv("LOCALE")
    return f"{get_greeting(locale)} {username}"
