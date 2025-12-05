import re


def parse_expression(expr: str):
    """
    Parse an expression in the form "a + b" and return (a, op, b).
    Supports +, -, *, / and floating-point numbers with optional sign.
    """
    pattern = r"^\s*([-+]?\d*\.?\d+(?:e[-+]?\d+)?)\s*([+\-*/])\s*([-+]?\d*\.?\d+(?:e[-+]?\d+)?)\s*$"
    match = re.match(pattern, expr, re.IGNORECASE)
    if not match:
        return None
    left, op, right = match.groups()
    return float(left), op, float(right)


def calculate(a: float, op: str, b: float):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
    raise ValueError(f"Unsupported operator: {op}")


def main():
    print('Введите выражение для вычисления или введите "exit" для выхода.')
    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() == "exit":
            print("Выход.")
            break

        parsed = parse_expression(user_input)
        if not parsed:
            print('Ошибка ввода. Используйте формат "a + b" с операциями + - * /.')
            continue

        a, op, b = parsed
        try:
            result = calculate(a, op, b)
            print(f"Результат: {result}")
        except ZeroDivisionError as exc:
            print(f"Ошибка: {exc}")
        except Exception as exc:  # noqa: BLE001
            print(f"Ошибка: {exc}")


if __name__ == "__main__":
    main()

