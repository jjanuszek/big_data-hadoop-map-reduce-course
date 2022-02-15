from mrjob.job import MRJob
import re

class MRSWordCount(MRJob):

    def mapper(self, _, line):
        WORD_RE = re.compile(r'[\w]+')
        words = WORD_RE.findall(line)
        for word in words:
            yield word.lower(), 1

    def reducer(self, key, values):
         yield key, sum(values)


if __name__ == '__main__':
    MRSWordCount.run()