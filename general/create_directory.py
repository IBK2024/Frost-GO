from os import makedirs


# !Create a directory
def create_directory(directory_name: str) -> None:
    """Creates directory"""
    makedirs(directory_name)
