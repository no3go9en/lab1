#import
from .lib import add, multiply


def main() -> None:
    """Головна точка входу: виконує виклики функцій з модуля lib та виводить результат."""
    x = 5
    y = 3

    print("Додавання:", add(x, y))
    print("Множення:", multiply(x, y))


if __name__ == "__main__":
    main()