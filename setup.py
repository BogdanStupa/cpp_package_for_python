import os

import pybind11
from distutils.core import setup, Extension


DIR_NAME = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(DIR_NAME, 'README.md')) as f:
    long_description = f.read()

path_to_src = os.path.join('src', 'cpp_package_for_python')

ext_modules = [
    Extension(
        'cpp_package_for_python', 
        sources=[
            os.path.join(path_to_src, 'library.cpp'),
            os.path.join(path_to_src, 'main.cpp'),
        ], 
        include_dirs=[pybind11.get_include()], 
        language='c++',
        extra_compile_args=['-std=c++17'], 
    ),
]

setup(
    name='cpp_package_for_python',
    version='0.0.1',
    # url="https://github.com/judy2k/helloworld",
    author='user',
    author_email='user@user.com',
    description='pybind11 extension',
    long_description=long_description,
    ext_modules=ext_modules,
    requires=['pybind11'],
    python_requires=">=3.7",
    # install_requires=["wheel"],
)