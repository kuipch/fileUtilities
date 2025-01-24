from pathlib import Path
import os
import sys


def check_dir_is_valid(directory):
    path = Path(directory)
    return Path.is_dir(path)

def get_directory(arguments):
    if len(arguments) > 1 and arguments[1] != "":
        return arguments[1]
    else:
        return os.getcwd()


def find_oldest_file(arguments):

    newest = False
    if '-n' in arguments:
        newest = True
        arguments.remove('-n')

    if '--newest' in arguments:
        newest = True
        arguments.remove('--newest')

    comparitor = find_oldest

    if newest:
        comparitor = find_newest

    directory = get_directory(arguments)
    oldest_file = None
    if check_dir_is_valid(directory):
        oldest_file = walk_directories(directory, comparitor)
    print(oldest_file)

def find_oldest_file_in_dir(directory, oldest_date,oldest_file, comparitor):
    path = Path(directory)

    try:
        for file in path.iterdir():
            current_file_date = os.path.getmtime(str(file))

            if file.is_file() and (comparitor(oldest_date,current_file_date)):
                oldest_file = file
                oldest_date = current_file_date
        return (oldest_date,oldest_file)
    except PermissionError:
        print(f"Note: directory {directory} skipped as not accessible")
        return (oldest_date,oldest_file)

def walk_directories(directory, comparitor):
    oldest_file = None
    oldest_date = None
    oldest_date, oldest_file = find_oldest_file_in_dir(directory, oldest_date,oldest_file, comparitor)

    for (root, dirs, files) in os.walk(directory):
        for directory in dirs:
            current_path = f"{root}\\{directory}"
            oldest_date, oldest_file = find_oldest_file_in_dir(current_path, oldest_date,oldest_file, comparitor)
    return oldest_file

def find_oldest(first_date, second_date) -> bool:
    return first_date is None or first_date > second_date

def find_newest(first_date, second_date) -> bool:
    return first_date is None or first_date < second_date

if __name__ == "__main__":
    find_oldest_file(sys.argv)
