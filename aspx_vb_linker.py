import os
import re
import sys

relative_path_read = sys.argv[1]
absolute_path_read = os.path.abspath(relative_path_read)
root_dir = os.path.dirname(absolute_path_read) + "\\"
regx_pattern = r'^<!-- #[Ii]nclude file="(.*)" -->'

def read_file(read_file_str, write_file):
    curr_dir = os.path.dirname(read_file_str) + "\\"
    
    file_note = f"' FILE: {read_file_str}\n"
    end_file_note = f"\n' END FILE: {read_file_str}\n\n\n"
    write_file.write(file_note)

    with open(read_file_str) as f:
        for line in f:
            match = re.match(regx_pattern, line)
            if match:
                # print(line)
                print(match.group(1))
                read_file(curr_dir + match.group(1), write_file)
                write_file.write(file_note)
            else:
                write_file.write(line)

    write_file.write(end_file_note)


def main():
    write_dir = root_dir + "build\\"
    write_file = write_dir + "linked.aspx"

    if not os.path.isdir(write_dir):
        os.mkdir(write_dir)

    if os.path.isfile(write_file):
        os.remove(write_file)

    with open(write_file, 'a') as out_file:
        read_file(absolute_path_read, out_file)
    # print(relative_path)
    # print(absolute_path)
    # print(root_dir)


if __name__ == "__main__":
    main()
