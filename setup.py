from setuptools import setup, find_packages

setup(
    name='mysite',
    packages=find_packages(),
    install_requires=['django-mako-plus'],
    extras_require={'tests': ['pytest']}
)