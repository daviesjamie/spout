from streams import BufferedStream, Stream
from multiprocessing import Process
from twython import TwythonStreamer
import json
import sys


class FileInputStream(Stream):
    """
    Loads the lines of a text file into a Stream for processing.
    """

    def __init__(self, filename):
        self.input = open(filename, 'r')
        self.next_line = None

    def has_next(self):
        if self.next_line is not None:
            return True

        try:
            self.next_line = self.input.next()
        except StopIteration:
            self.next_line = None

        return self.next_line is not None

    def next(self):
        if not self.has_next():
            raise Exception("No more elements in file!")

        to_return = self.next_line
        self.next_line = None

        return to_return

    def __del__(self):
        self.input.close()


class JSONInputStream(FileInputStream):
    """
    Loads a file containing a separate JSON object on each line into a Stream for processing.
    """

    def __init__(self, filename):
        super(JSONInputStream, self).__init__(filename)

    def next(self):
        return json.loads(super(JSONInputStream, self).next())

    def __del__(self):
        super(JSONInputStream, self).__del__()


class TweetStream(BufferedStream):
    """
    Publishes tweets fetched from the Twitter Sample stream to a BufferedStream for processing.
    """
    def __init__(self, buf, app_key, app_secret, access_token, access_token_secret):
        super(TweetStream, self).__init__(buf)
        self.source = self.TweetSource(self, app_key, app_secret, access_token,
                                       access_token_secret)
        self.worker = Process(target=self.source.statuses.sample)
        self.worker.daemon = True

    def connect(self):
        super(TweetStream, self).connect()
        self.worker.start()

    def disconnect(self):
        super(TweetStream, self).disconnect()

        self.source.disconnect()
        self.worker.terminate()


    class TweetSource(TwythonStreamer):
        """
        Acts as the 'listener' to the official Twitter Sample stream.
        """
        def __init__(self, publish_stream, app_key, app_secret, access_token, access_token_secret):
            super(TweetStream.TweetSource, self).__init__(app_key, app_secret, access_token,
                                                          access_token_secret)
            self.publish_stream = publish_stream

        def on_success(self, data):
            if 'text' in data:
                self.publish_stream.register(data)

        def on_error(self, status_code, data):
            sys.stderr.write('{0} - {1}'.format(status_code, data))

