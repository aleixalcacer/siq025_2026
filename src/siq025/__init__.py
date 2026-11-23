from datetime import date


def main() -> None:
    print(f"Hola Aleix, hui es {date.today():%d/%m/%Y}")
