from typing import Iterable


def ban_users(users_ids: Iterable[int]) -> int:
    pass


if __name__ == "__main__":
    assert ban_users(users_ids={167, 623, 209, 921}) == 2
