from datetime import date


def main() -> None:
    print(f"Hola Aleix, hui és {date.today():%d/%m/%Y}")
