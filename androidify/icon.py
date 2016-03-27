import os
import sys
import shutil
from PIL import Image

OUT_FILENAME = 'ic_launcher.png'

sizes = {
    'mipmap-hdpi': (72, 72),
    'mipmap-mdpi': (48, 48),
    'mipmap-xhdpi': (96, 96),
    'mipmap-xxhdpi': (144, 144),
    'mipmap-xxxhdpi': (192, 192)
}

def resize(input_file, output_directory, size):
    print('\tresizing {} to {} ({} x {}) ...'.format(input_file, output_directory, size[0], size[1]), end=' ')

    os.mkdir(output_directory)

    outfile = "{}/{}".format(output_directory, OUT_FILENAME)

    im = Image.open(input_file)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile, "PNG")

    print('done')

def main():
    if len(sys.argv) != 2:
        raise Exception('Expected exactly one argument with image filename')

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        raise Exception('File "{}" does not exist'.format(input_file))

    print('resizing {} ...'.format(input_file))

    if os.path.exists('out'):
        shutil.rmtree('out')

    os.mkdir('out')

    for size in sizes:
        resize(input_file, 'out/{}'.format(size), sizes[size])

if __name__ == '__main__':
    main()
