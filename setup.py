from glob import glob
from os.path import basename
from os.path import splitext

import setuptools


setuptools.setup(
    name='kosmosquest-ng',
    version='0.1-beta',
    url='https://github.com/mahmoudimus/kosmosquest-ng',
    license='Apache License 2.0',
    author='mahmoudimus',
    author_email='mahmoud - @ - linux.com',
    description='kosmosquest-ng -- an open source implementation of cosmos quest',
    packages=setuptools.find_packages('.'),
    package_dir={'': '.'},
    py_modules=[splitext(basename(path))[0] for path in glob('./*.py')],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)