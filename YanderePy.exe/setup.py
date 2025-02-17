# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='',
    ext_modules=cythonize("CppGame.py", build_dir="build"),
)
