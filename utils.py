import collections
import itertools
import random


def generate_random_nucleotides(options=('A', 'T', 'G', 'C', 'N')):
    """Generates random nucleotides

    :param options: Possible nucleotides
    :return: an iterator over random ones

    >>> import itertools, random
    >>> random.seed(42)
    >>> list(itertools.islice(generate_random_nucleotides(), 8))
    ['A', 'A', 'G', 'T', 'T', 'T', 'A', 'N']
    """
    while True:
        yield random.choice(options)


def group_nucleotides(nucleotides):
    """ Combines 'A' & 'T' into 'AT', 'G' & 'C' into 'GC', and leaves 'N' alone
    :return: an iterator

    >>> test_nucleotides = ['A', 'A', 'G', 'T', 'T', 'T', 'A', 'N', 'C']
    >>> list(group_nucleotides(test_nucleotides))
    ['AT', 'AT', 'GC', 'AT', 'AT', 'AT', 'AT', 'N', 'GC']
    """
    nucleotide_group_map = {
        'A': 'AT',
        'T': 'AT',
        'G': 'GC',
        'C': 'GC',
        'N': 'N'
    }
    for nucleotide in nucleotides:
        yield nucleotide_group_map[nucleotide]


def sliding_percentages(items, window_size, unique_items):
    """Generates a sliding window of percentages for items in an iterator

    :return: an iterator over windowed percentages
    >>> test_nucleotide_groups = ['AT', 'AT', 'GC', 'AT', 'AT', 'AT', 'AT', 'N', 'GC']
    >>> percentages = list(sliding_percentages(test_nucleotide_groups, 4, ('AT', 'GC', 'N')))
    >>> import pprint
    >>> pprint.pprint(percentages)
    [{'AT': 0.75, 'GC': 0.25, 'N': 0.0},
     {'AT': 0.75, 'GC': 0.25, 'N': 0.0},
     {'AT': 0.75, 'GC': 0.25, 'N': 0.0},
     {'AT': 1.0, 'GC': 0.0, 'N': 0.0},
     {'AT': 0.75, 'GC': 0.0, 'N': 0.25},
     {'AT': 0.5, 'GC': 0.25, 'N': 0.25}]
    """
    item_window = collections.deque(itertools.islice(items, window_size), maxlen=window_size)
    # Set the count values to 0 for the unique items which can occur
    counter = collections.Counter({item: 0 for item in unique_items})
    # Update the counter from the first window
    counter.update(item_window)
    # Calculate and the first window's percentages
    window_percentage = {key: value / window_size for key, value in counter.items()}
    yield window_percentage
    # Start iterating over items, starting at the first item after the first window
    for item in itertools.islice(items, window_size, None):
        # Take the trailing item from the left of the window
        trailing_item = item_window.popleft()
        # Subtract the counter for the trailing, dropped item
        counter.subtract([trailing_item])
        # Add the new item to the right of the window
        item_window.append(item)
        # Update the counter for the new, added item
        counter.update([item])
        # Calculate and yield the current window's percentages
        window_percentage = {key: value / float(window_size) for key, value in counter.items()}
        yield window_percentage
