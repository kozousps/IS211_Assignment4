import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return(a_list)


def sequential_search(a_list, item):
    """
    Performs search from first index to last

    :params: a_list: Original list from get_me_random_list(n)
             item: Number to search for
    :returns: True(found) or False(Not Found)
    """
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1
    return found


def ordered_sequential_search(a_list, item):
    """
    Performs search from first index to last in ordered list

    :params: a_list: Original list from get_me_random_list(n)
             item: Number to search for
    :returns: True(found) or False(Not Found)
    """
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1
    return(found)


def binary_search_iterative(a_list, item):
    """
    Performs search from middle item in ordered list and eliminates half that
        does not contain number

    :params: a_list: Original list from get_me_random_list(n)
             item: Number to search for
    :returns: True(found) or False(Not Found)
    """
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def binary_search_recursive(a_list, item):
    """
    Performs search from middle item in ordered list and eliminates half that
        does not contain number with recursion

    :params: a_list: Original list from get_me_random_list(n)
             item: Number to search for
    :returns: True(found) or False(Not Found)
    """
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def main(n, item):

    t0 = 0
    for i in range(100):
        b_list = get_me_random_list(n)
        start = time.time()
        a1 = sequential_search(b_list, item)
        end = time.time()
        t1 = end-start
        t0 += t1
    avgt = t0/100
    print("Sequential Search result was {} and took {:10.7f} "
          .format(a1, avgt) + "seconds to run, on average.")

    t0 = 0
    for i in range(100):
        b_list = get_me_random_list(n)
        sorted(b_list)
        start = time.time()
        a2 = ordered_sequential_search(b_list, item)
        end = time.time()
        t1 = end-start
        t0 += t1
    avgt = t0/100
    print("Ordered Sequential Search result was {} and took {:10.7f} "
          .format(a2, avgt) + "seconds to run, on average.")

    t0 = 0
    for i in range(100):
        b_list = get_me_random_list(n)
        sorted(b_list)
        start = time.time()
        a3 = binary_search_iterative(b_list, item)
        end = time.time()
        t1 = end-start
        t0 += t1
    avgt = t0/100
    print("Binary Search Iterative result was {} and took {:10.7f} "
          .format(a3, avgt) + "seconds to run, on average.")

    t0 = 0
    for i in range(100):
        b_list = get_me_random_list(n)
        sorted(b_list)
        start = time.time()
        a4 = binary_search_recursive(b_list, item)
        end = time.time()
        t1 = end-start
        t0 += t1
    avgt = t0/100
    print("Binary Search Recursive result was {} and took {:10.7f} "
          .format(a4, avgt) + "seconds to run, on average. \n")


if __name__ == "__main__":
    """Main entry point"""
    L = [500, 1000, 5000]
    counter = 0
    for i in L:
        print("For list size: {}".format(L[counter]))
        main(L[counter], -1)
        counter += 1
