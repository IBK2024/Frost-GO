from os import makedirs


# !Create a directory
def createDirectory(directoryName: str) -> None:
    makedirs(directoryName)
