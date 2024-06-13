from os import makedirs


# !Create a directory
def create_directory(directory_name: str) -> None:
    makedirs(directory_name)
