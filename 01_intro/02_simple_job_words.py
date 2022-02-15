from mrjob.job import MRJob
from mrjob.step import MRStep

class MRSimpleJobWords(MRJob):

    # pomaga w debugowaniu
    # def steps(self):
    #     return [
    #         MRStep(mapper=self.mapper,
    #                reducer=self.reducer)
    #     ]

    def mapper(self, _, line):
        yield 'nomber_of_lines', 1
        yield 'nomber_of_words', len(line.split())
        yield 'chars', len(line)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRSimpleJobWords.run()
