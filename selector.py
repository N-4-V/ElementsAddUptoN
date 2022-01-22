"""Program Solution Functionalities"""
import itertools


def binary_generation(length_of_binary, number_of_ones):
    """Returns the indexes at which 1 occurs for All binary numbers of given length with given no. of 1's in them"""
    all_indexes = []

    for bits in itertools.combinations(range(length_of_binary), number_of_ones):
        indexes_of_ones = []

        for bit in bits:
            # Say, b is a binary string where b = ["0"]*length | Then, b[bit] would be "1"
            indexes_of_ones.append(bit)

        # indexes at which 1's occur in b get appended
        all_indexes.append(indexes_of_ones)
    return all_indexes


def solution_subsets(array, subset_size, target_sum):
    """Returns all possible solutions that add upto the target sum for a specified size"""

    # returns all binary numbers with given length with given no. of 1's
    all_binary_numbers = binary_generation(len(array), subset_size)
    solutions = []

    for each_binary_number in range(len(all_binary_numbers)):

        # Stores sum of superimposition of array values onto binary number representation at positions of 1's
        corresponding_sum = 0
        # stores the values themselves
        solution_values = "[ "

        for corresponding_value in range(len(all_binary_numbers[each_binary_number])):
            try:
                corresponding_sum += array[ all_binary_numbers[each_binary_number][corresponding_value] ]

            # in case 'NULL' is passed in array
            except TypeError:
                corresponding_sum += 0

            solution_values += str(array[ all_binary_numbers[each_binary_number][corresponding_value] ]) + " "

        # if sum 's' is equal to user-specified sum,the solution gets added to the list to be returned
        if corresponding_sum == target_sum:
            solution_values += "]"
            solutions.append(solution_values)
    return solutions


def viable_solutions(array, target_sum):
    """Displays all subsets that add upto target_sum"""
    all_solutions = []
    number_of_solutions = 0

    for subset_size in range(1, len(array) + 1):
        # Finds solutions for each subset length
        solutions_for_subset = solution_subsets(array, subset_size, target_sum)

        # If solutions exist for the subset of a particular size
        if len(solutions_for_subset) != 0:
            all_solutions.append(solutions_for_subset)
            number_of_solutions += len(solutions_for_subset)

    return all_solutions, number_of_solutions
