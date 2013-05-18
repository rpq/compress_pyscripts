import glob
from distutils.core import setup

with open('PYPI_CLASSIFIERS.txt') as f:
    PYPI_CLASSIFIERS = filter(None, f.read().split('\n'))
with open('README.md') as f:
    README = f.read()

data_files = ['MIT_LICENSE.txt', 'REQUIREMENTS.txt', 'README.md',
    'PYPI_CLASSIFIERS.txt',]

script_files = glob.glob('src/scripts/*')

setup(
    name='compress_pyscripts',
    version='0.0.1',
    url='https://github.com/rpq/compress_pyscripts',
    data_files=[
        ('django_deploys', data_files),],

    scripts=script_files,

    description='Compression related scripts',
    long_description=README,
    license='MIT_LICENSE.txt',
    classifiers=PYPI_CLASSIFIERS,

    author='Ramon Paul Quezada',
    author_email='rpq@winscores.com',
)
