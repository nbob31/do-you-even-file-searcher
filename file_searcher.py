import argparse
import os


def parse_arguments():
    args = argparse.ArgumentParser()
    args.add_argument('-p', '--path', required=True, help="File path used for a recursive search")
    args.add_argument('-t', '--text', required=True, help="Target text to search for")
    return args.parse_args()


def find_supported_files(path):
    matching_files = []
    supported_file_types = ['.go', '.java', '.rb', '.py', '.html', '.js', '.txt', '.rtf', '.yaml',
                            '.yml', '.docx', '.pdf', '.scala', '.kt', '.tf']
    for dir_path, dir_name, filenames in os.walk(path):
        for file in filenames:
            for supported_file_type in supported_file_types:
                if file.endswith(supported_file_type):
                    matching_files.append(
                        os.path.abspath(
                            os.path.join(
                                dir_path, file
                            )
                        )
                    )
    return matching_files


def open_files_and_search(files, search_text):
    """
    Opens and searches the file for specific search text
    :param files: specific files to search
    :param search_text: String to search for
    :return: found matches
    """
    matches = []
    for file_path in files:
        with open(file_path, encoding="utf8", errors='ignore') as file:
            file_content = file.readlines()
        for line_number, line in enumerate(file_content):
            if search_text in line:
                matches.append((file_path, line_number + 1))
    return matches


def search_file_system():
    args = parse_arguments()
    full_path = os.path.abspath(args.path)
    supported_files = find_supported_files(full_path)
    matches = open_files_and_search(supported_files, args.text)
    if matches:
        print(f"The string {args.text} has been found at the following places ...")
        for match in matches:
            file_path, line_number = match
            print(f'{file_path} at line {line_number}')
    else:
        print(f'No matches found when searching files for {args.text} at {full_path}')


if __name__ == '__main__':
    search_file_system()
