from setuptools import setup

setup(
    name="spout",
    version="0.1.6",
    author="Jamie Davies",
    author_email="jamie@jamiedavies.me",
    packages=['spout'],
    url="http://github.com/daviesjamie/spout",
    license="MIT",
    description="A simple framework that makes it easy to work with data streams in Python.",
    install_requires=[
        "twython >= 3.1.2"
    ],
    long_description="""
Spout is a small and simple framework that makes it easy to work with data
streams in Python. In particular, Spout was designed with the processing and
consumption of live data sources in mind.


How it works
------------

At the heart of Spout is the concept of a Stream (which is defined in an
abstract `Stream` class). This defines the basic operations that can be
performed upon a data stream:

Mapping
    The items in one stream can be "mapped" to another stream. This is done by
    applying a supplied Function to each item in the input stream, to produce
    another output stream.

    stream.map(Function)

Filtering
    The items in a stream can be "filtered", so that the resultant stream only
    contains items that match a given criteria. This is done by using a supplied
    Predicate to test each item in the input stream, and copies it to the output
    stream if it passes the test criteria.

    stream.filter(Predicate)

Processing (Consuming)
    The items in a stream are used in some calculations or functionality that
    provides no further output to the stream. This is done by applying the supplied
    Operation to each item in the stream.

    stream.for_each(Operation)


Usage
-----

To use Spout, you first need to create an input data stream. A data stream is simply an
instantiation of a Stream or any of its children (which can be found in the
streams.py file). The Stream class has been specifically designed so that it
is easy to extend and wrap around currently existing data sources that you might
have, such as files or databases.

Some existing examples of stream data sources can by found in sources.py.

For example, to create a Stream out of the lines in a plain text file:

    from spout.sources import FileInputStream
    s = FileInputStream("test.txt")

Now that you have your data in a stream, you simply have to process it! This can
be done by creating and using your own Functions, Predicates or Operations
(see above).

For example, to print out all the lines in a text file that start with a digit,
but with the digit stripped, we can create our own Predicate and Function
and pass these to the .filter() and .map() functions:

    from spout.sources import FileInputStream
    from spout.structs import Function, Predicate
    from spout.outputs import PrintOperation


    class StartsWithDigit(Predicate):
        def test(self, obj):
            return obj[0].is_digit()


    class StripFirstChar(Function):
        def apply(self, input):
            return input[1:]


    s = FileInputStream("test.txt")
    s \
        .filter(StartsWithDigit()) \
        .map(StripFirstChar()) \
        .for_each(PrintOperation())


Installation
------------

Spout is available in the Python Package Index (PyPI), and so the easiest way to
install it is through pip:

    $ pip install spout

However, it is also possible to install the repository from the source, through
the setup.py utility:

    $ python setup.py install


Credits
-------

The inspiration for Spout's fluent interface came largely from the OpenIMAJ streaming framework.
http://www.openimaj.org/
""",
)
