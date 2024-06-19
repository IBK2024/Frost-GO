from typing import Literal, Set


def parse_robot_txt(url: str) -> Literal[True] | Set[Literal[False] | str]:
    """Parse robots.txt of the provided link"""
    return {False, url}
