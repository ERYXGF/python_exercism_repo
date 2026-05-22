def append(list1, list2):
    """Add all items in the second list to the end of the first list."""
    result = []
    for item in list1:
        result += [item]
    for item in list2:
        result += [item]
    return result


def concat(lists):
    """Given a series of lists, combine all items into one flattened list."""
    result = []
    for sublist in lists:
        for item in sublist:
            result += [item]
    return result


def filter(predicate, list):
    """Return the list of all items for which predicate(item) is True."""
    result = []
    for item in list:
        if predicate(item):
            result += [item]
    return result


def length(list):
    """Return the total number of items within the list."""
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    """Return the list of results of applying function(item) on all items."""
    result = []
    for item in list:
        result += [function(item)]
    return result


def foldl(function, list, initial):
    """Fold each item into the accumulator from the left."""
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    """Fold each item into the accumulator from the right.
    
    Note: Pass (accumulator, item) to match the test suite's lambda structure.
    """
    accumulator = initial
    # Loop backwards from the last index down to 0
    for i in range(length(list) - 1, -1, -1):
        accumulator = function(accumulator, list[i])
    return accumulator


def reverse(list):
    """Return a list with all the original items, but in reversed order."""
    result = []
    # Build the list backwards by inserting elements in reverse order
    for i in range(length(list) - 1, -1, -1):
        result += [list[i]]
    return result