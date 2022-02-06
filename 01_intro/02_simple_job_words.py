from mrjob.job import MRJob


class MRSimpleJobWords(MRJob):

    def mapper(self, _, line):
        yield 'nomber_of_words', len(line.split())
        yield 'nomber_of_lines', 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRSimpleJobWords.run()