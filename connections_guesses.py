'''' Function that returns how many ways to choose r items from the first '''
def combinations(items, r):
    if r == 0:
        return [[]]
    if len(items) < r:
        return[]
    first, rest = items[0], items[1:]
    with_first = [[first] + c for c in combinations(rest, r - 1)]
    return with_first + combinations(rest, r)



''' Function that calculates how many guesses are needed to guarantee 
finding all categories in the worst-case of guessing '''
def guesses_needed(categories, words_per_category, solved=0):
    m, k = words_per_category, categories - solved
    if k <= 1:
        return 0

    def partitions(pool):
        pass
