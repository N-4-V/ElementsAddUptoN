import sys
import itertools

def kbits(n, k): # generates all n-bit binary numbers with k 1's in it, and returns indexes of those 1's
	z = []
	for bits in itertools.combinations(range(n), k):
		ones = []
		b = ["0"] * n
		for bit in bits:
			# b[bit] = "1" 
			ones.append(bit) 
		z.append(ones) # appends the indexes at which 1 occurs in b
	return z

def sums(a, k, N): # a is the list, k is the defined length of the subset, N is the sum specified by user 
	b = kbits(len(a), k)
	z = []
	for i in range(len(b)):
		s = 0 # stores sum of values at indexes in 'a' corresponding to the indexes of 1's according to 'b' 
		v = "" # stores the values themselves
		for j in range(len(b[i])):
			s += a[b[i][j]]
			v += str(a[b[i][j]]) + " "
		if s == N: # if sum 's' is equal to user-specified sum, then the solution gets added to the list to be returned
			z.append(v)
	return z

def disp(z): # displays all elements of a given list
	for i in z:
		print(i)

a = list(map(int, sys.stdin.readline().split())) # takes list as input from user in format: 5 10 3 2 -5 4 1
N = int(sys.stdin.readline()) # total to be acquired through summation of elements 
k = int(sys.stdin.readline()) # length of subset 


if k != 0: # if k is specified, only display subsets with k elements in them
	z = sums(a, k, N)
	disp(z)

else: # display all subsets which could add up to N
	for i in range(1, len(a)+1):
		z = sums(a, i, N)
		disp(z)
