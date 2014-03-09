from setuptools import setup

setup(
    name="spout",
    version="0.1.1",
    author="Jamie Davies",
    author_email="jamie@jamiedavies.me",
    packages=['spout'],
    url="http://github.com/daviesjamie/spout",
    license="MIT",
    description="A simple framework that makes it easy to work with data streams in Python.",
    long_description=open('README.md').read(),
    install_requires=[
        "twython >= 3.1.2"
    ],
)
