from os import listdir, getcwd, rename
from os.path import isfile, join

from_end = 'dat'
to_end = 'aml'

if __name__ == "__main__":
    print('Path=', end='')
    path = getcwd()
    print(path + '\nScanning', end='')
    files = [f for f in listdir(path) if isfile(join(path, f))]
    print(' OK')
    i = 0
    for file in files:
        file_split = file.split('.')
        if file_split[-1] == from_end:
            file_split = file_split[:-1]
            new_file = ''
            for s in file_split:
                new_file += s
            new_file += '.' + to_end
            print(f'{i}. {file} -> {new_file}')
            rename(file, new_file)
            i += 1
    if i == 0:
        print('No file renamed!')