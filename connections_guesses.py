# Function that returns how many ways to choose r items from the first
def combinations(items, r):
    if r == 0:
        return [[]]
    if len(items) < r:
        return[]
    first, rest = items[0], items[1:]
    with_first = [[first] + c for c in combinations(rest, r - 1)]
    return with_first + combinations(rest, r)
