import itertools
import random

import utils

NUCLEOTIDE_GROUPS = ('AT', 'GC', 'N')


def test_percentages(number_of_nucleotides, window_size, output):
    output.write('\t'.join(NUCLEOTIDE_GROUPS))
    output.write('\n')
    nucleotides = utils.generate_random_nucleotides()
    nucleotide_groups = utils.group_nucleotides(nucleotides)
    nucleotide_groups_limited = itertools.islice(nucleotide_groups, number_of_nucleotides)
    sliding_percentages = utils.sliding_percentages(nucleotide_groups_limited,
                                                    window_size,
                                                    NUCLEOTIDE_GROUPS)
    for percentages in sliding_percentages:
        output.write('\t'.join([str(percentages[group_key]) for group_key in NUCLEOTIDE_GROUPS]))
        output.write('\n')


if __name__ == '__main__':
    random.seed(42)
    with open('out.tsv', 'w') as output:
        test_percentages(3000000, 300, output)
