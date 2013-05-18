#!/usr/bin/env python
import os
import argparse

def prepend_text_to_extension(text, prepend_text='.min.'):
    array_text = []

    if '.' not in text:
        raise Exception('The text argument expects an filename and extension separated by a period.')

    if '/' in text:
        front, full_filename = os.path.split(text)
        array_text.extend([front, '/'])

    filename, extension = full_filename.split('.')
    array_text.extend(['/', filename, prepend_text, extension])
    return ''.join(array_text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='concatenates files into one file based on args given')
    parser.add_argument('-c', '--compressor', dest='compressor',
        help='compressor path')
    parser.add_argument('-r', '--root', dest='root', help='root of path',
        required=True)
    parser.add_argument('-f', '--files', nargs='+', dest='files',
        help='files on root path', required=True)
    parsed_args = parser.parse_args()

    COMPRESSOR_PATH = parsed_args.compressor

    MEDIA_PATH = parsed_args.root
    MEDIA_FILES = parsed_args.files

    for file_name in MEDIA_FILES:
        full_path = os.path.join(MEDIA_PATH, file_name)
        new_full_path = prepend_text_to_extension(full_path)
        cmd = 'java -jar {0} {1} -o {2}'.format(
            COMPRESSOR_PATH, full_path, new_full_path)
        print 'compressing {0} to {1}...'.format(
            os.path.split(full_path)[1],
            os.path.split(new_full_path)[1])
        os.system(cmd)
