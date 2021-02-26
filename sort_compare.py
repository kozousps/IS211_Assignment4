import random
import time


def get_me_random_list(n):
    """Generate list of n elements in random order

    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n+1))
    random.shuffle(a_list)
    return(a_list)


def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value


def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return a_list


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(a_list):
    return sorted(a_list)


def main(n):
    t0 = 0
    for i in range(100):
        a_list = get_me_random_list(n)
        start = time.time()
        insertion_sort(a_list)
        end = time.time()
        t1 = end-start
        t0 += t1
    avgt = t0/100

    print("Insertion Sort result took {:10.7f} seconds to run, on average."
          .format(avgt))

    t0 = 0
    for i in range(100):
        a_list = get_me_random_list(n)
        start = time.time()
        shell_sort(a_list)
        end = time.time()
        t1 = end-start
        t0 += t1
    avgt = t0/100

    print("Shell Sort result took {:10.7f} seconds to run, on average."
          .format(avgt))

    t0 = 0
    for i in range(100):
        a_list = get_me_random_list(n)
        start = time.time()
        python_sort(a_list)
        end = time.time()
        t1 = end-start
        t0 += t1
    avgt = t0/100

    print("Python Sort result took {:10.7f} seconds to run, on average. \n"
          .format(avgt))


if __name__ == "__main__":
    """Main entry point"""
    L = [500, 1000, 5000]
    counter = 0
    for i in L:
        print("For list size: {}".format(L[counter]))
        main(L[counter])
        counter += 1
