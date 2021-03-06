from glob import glob
from distutils.extension import Extension
from os.path import pathsep
from setuptools import setup, find_packages
import numpy as np

# Use cython only if *.pyx files are present (i.e., not in sdist)
ext_paths = ('dstrf/*%s', 'dstrf/dsyevh3C/*%s')
if glob(ext_paths[0] % '.pyx'):
    from Cython.Build import cythonize

    ext_modules = cythonize([path % '.pyx' for path in ext_paths])
else:
    actual_paths = []
    for path in ext_paths:
        actual_paths.extend(glob(path % '.c'))
    ext_modules = [
        Extension(path.replace(pathsep, '.')[:-2], [path])
        for path in actual_paths
    ]

setup(
    name="dstrf",
    description="MEG/EEG analysis tools",
    version="0.1",
    packages=find_packages(),
    python_requires='>=3.0',

    install_requires=[
        'numpy',
        'scipy',
        'eelbrain',
    ],


    # metadata for upload to PyPI
    author="Proloy DAS",
    author_email="proloy@umd.com",
    license="apache 2.0",
    include_dirs=[np.get_include()],
    ext_modules=ext_modules,
    project_urls={
        "Source Code": "https://github.com/proloyd/fastapy",
    }
)
