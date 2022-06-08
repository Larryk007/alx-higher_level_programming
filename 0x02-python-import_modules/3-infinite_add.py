#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	display = 0
	i = len(sys.argv)
	for arg in sys.argv:
		if arg != sys.argv[0]:
			display = int(arg)
		print(display)
