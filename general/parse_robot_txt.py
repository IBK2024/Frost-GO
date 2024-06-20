from typing import Literal, Set


def parse_robot_txt(
    url: str | Literal[True],
) -> Literal[True] | Set[Literal[False] | str]:
    """Parse robots.txt of the provided link"""
    if url is True:
        return True
    return {False, url}
