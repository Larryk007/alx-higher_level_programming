#!/usr/bin/env python3
def print_matrix_integer(matrix = [[]]):
	for row in (matrix):
		for column in row:
			print("{:d}".format(column), end = " " if row[-1] != column else "")
		print()
