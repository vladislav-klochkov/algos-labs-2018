from random import random
import time

from TSP_branch_and_boundary import TSPBranchAndBoundary
from TSP_local_search import TSPLocalSearch
from TSP_simulated_annealing import TSPSimulatedAnnealing

NO_EDGE = -1
MAX_VAL = 999999999


def main():
    f = open("TSP/results.txt", "rw+")

    # arr, n = read_array()
    # print n, "\n", arr, "\n"
    # perform_comparison(arr, n, f)

    for i in range(10, 20):
        arr = generate_graph(10, 100)
        perform_comparison(arr, 10, f)

    f.close()


def perform_comparison(arr, n, f):
    f.write("\n\nGraph with " + str(n) + " vertices.\n")
    for i in range(n):
        f.write(str(arr[i]) + "\n")
    f.write("\n")

    # print "Simulated annealing(Koshi):"
    # f.write("\nSimulated annealing(Koshi):\n")
    # start_time = time.time()
    # res = TSPSimulatedAnnealing(arr).solve_koshi()
    # print res
    # f.write(str(res) + "\n")
    # tsp_sa_koshi_time = time.time() - start_time
    # print tsp_sa_koshi_time, "\n"
    # f.write(str(tsp_sa_koshi_time) + "\n")

    # print "Simulated annealing(Bolcman):"
    # f.write("\nSimulated annealing(Bolcman):\n")
    # start_time = time.time()
    # res = TSPSimulatedAnnealing(arr).solve_koshi()
    # print res
    # f.write(str(res) + "\n")
    # tsp_sa_bolcman_time = time.time() - start_time
    # print tsp_sa_bolcman_time, "\n"
    # f.write(str(tsp_sa_bolcman_time) + "\n")

    print "Brute force:"
    f.write("\nBrute force:\n")
    start_time = time.time()
    res = tsp_brute_force(arr, n)
    print res
    f.write(str(res) + "\n")
    tsp_brute_force_time = time.time() - start_time
    print tsp_brute_force_time, "\n"
    f.write(str(tsp_brute_force_time) + "\n")

    print "Greedy:"
    f.write("\nGreedy:\n")
    start_time = time.time()
    res = tsp_greedy(arr, n)
    print res
    f.write(str(res) + "\n")
    tsp_greedy_time = time.time() - start_time
    print tsp_greedy_time, "\n"
    f.write(str(tsp_greedy_time) + "\n")

    print "Branch and boundary:"
    f.write("\nBranch and boundary:\n")
    start_time = time.time()
    res = TSPBranchAndBoundary(arr).solve()
    print res
    f.write(str(res) + "\n")
    tsp_branch_and_boundary_time = time.time() - start_time
    print tsp_branch_and_boundary_time, "\n"
    f.write(str(tsp_branch_and_boundary_time) + "\n")

    # print "Local search(2 opt):"
    # f.write("\nLocal search(2 opt):\n")
    # start_time = time.time()
    # res = TSPLocalSearch(arr).solve_2_opt()
    # print res
    # f.write(str(res) + "\n")
    # tsp_local_search_2_time = time.time() - start_time
    # print tsp_local_search_2_time, "\n"
    # f.write(str(tsp_local_search_2_time) + "\n")

    # print "Local search(3 opt):"
    # f.write("\nLocal search(3 opt):\n")
    # start_time = time.time()
    # res = TSPLocalSearch(arr).solve_3_opt()
    # print res
    # f.write(str(res) + "\n")
    # tsp_local_search_3_time = time.time() - start_time
    # print tsp_local_search_3_time, "\n"
    # f.write(str(tsp_local_search_3_time) + "\n")


def generate_graph(n, max_val):
    return [[int(random() * max_val + 1) if i != j else NO_EDGE for j in range(n)] for i in range(n)]


def read_array():
    input_file = open("TSP/TSP.txt", "r")
    n = int(input_file.readline())
    arr = []

    for _ in range(n):
        arr.append([int(x) for x in input_file.readline().split()])

    return arr, n


def generate_permutations(array, low=0):
    if low + 1 >= len(array):
        yield array
    else:
        for p in generate_permutations(array, low + 1):
            yield p
        for i in range(low + 1, len(array)):
            array[low], array[i] = array[i], array[low]
            for p in generate_permutations(array, low + 1):
                yield p
            array[low], array[i] = array[i], array[low]


def tsp_brute_force(array, n):
    path_cost = MAX_VAL
    path = []

    for permutation in generate_permutations(range(n), 1):
        length = len(permutation)
        temp_cost = 0

        for i in range(length - 1):
            temp_cost += array[permutation[i]][permutation[i + 1]]

        temp_cost += array[permutation[length - 1]][0]

        if temp_cost < path_cost:
            path = list(permutation)
            path_cost = temp_cost

    return path, path_cost


def tsp_greedy(array, n):
    path = [0]
    path_cost = 0
    prev_index = 0

    for i in range(n):
        min_val = MAX_VAL
        min_index = 0

        for j, item in enumerate(array[prev_index]):
            if prev_index != j and item < min_val:
                if i == n - 1:
                    min_val = item
                    min_index = j
                elif j not in path:
                    min_val = item
                    min_index = j

        prev_index = min_index
        path.append(min_index)
        path_cost += min_val

    return path, path_cost


main()
