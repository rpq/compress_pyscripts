#!env python

import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='concatenates files into one file based on args given')
    parser.add_argument('-r', '--root', dest='root', help='root of path',
        required=True)
    parser.add_argument('-f', '--files', nargs='+', dest='files',
        help='files on root path', required=True)
    parser.add_argument('-d', '--filename',
        default='single_optimized_file', dest='filename',
        help='filename to concat to', required=True)
    parsed_args = parser.parse_args()

    MEDIA_PATH = parsed_args.root
    MEDIA_FILES = parsed_args.files

    MEDIA_FILE_TO = os.path.join(MEDIA_PATH, parsed_args.filename)

    print 'concatenating files {0} to {1}'.format(' '.join(
        MEDIA_FILES), MEDIA_FILE_TO)
    os.system('cat {0} > {1}'.format(
        ' '.join([os.path.join(MEDIA_PATH, media_file) for media_file in MEDIA_FILES]), MEDIA_FILE_TO))
