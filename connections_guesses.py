'''' Function that returns how many ways to choose r items from the list '''
def combinations(items, r):
    if r == 0:
        return [[]]
    if len(items) < r:
        return[]
    first, rest = items[0], items[1:]
    with_first = [[first] + c for c in combinations(rest, r - 1)]
    return with_first + combinations(rest, r)



''' Function that returns how many ways to split the words into groups
of given size. '''
def all_groupings(words, size):
    if not words:
        return [frozenset()]
    first, rest = words[0], words[1:]
    result = []
    for others in combinations(rest, size - 1):
        group = frozenset([first] + others)
