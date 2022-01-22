"""Main driver to run Program"""
import selector as sL
import sys


try:
    print("\n Enter the Elements of the Array: ")
    # takes list as input from user in format: 5 10 3 2 -5 4 1
    array = list(map(int, sys.stdin.readline().split()))

    print("\n Enter the Target Sum: ")
    # total to be acquired through summation of elements
    target_sum = int(sys.stdin.readline())

    solutions, number_of_solutions = sL.viable_solutions(array, target_sum)
    if number_of_solutions == 0:
        print("\nThere are No Solutions for the given problem.")
    else:
        print("\nFollowing are the List of Subsets in increasing order of their lengths:")
        for solution in solutions:
            # formatting elements are removed from total length of each solution to get its subset size
            print("\nLength " + str(len(solution[0]) -
                                    solution[0].count(" ") - solution[0].count("-") - 2) + " solutions : ", end="")
            for subsets in solution:
                print(subsets, end="\t\t")

except ValueError:
    # if user gives alphabets in input
    print("\nValue Invalid. Input should only have Numbers.")
except IndexError:
    # if user gives alphabets in input
    print("\nError. Input cannot be Empty.")
