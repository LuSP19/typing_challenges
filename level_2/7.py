from typing import Iterable


def calculate_total_spent_for_user(
    user: tuple[str, int, Iterable[int]]
) -> int:
    pass


if __name__ == "__main__":
    assert calculate_total_spent_for_user(user=("Ilya", 32, [102, 15, 63, 12])) == 192
