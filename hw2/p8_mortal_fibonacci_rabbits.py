
def fib(n, m):
	rabbits = [1] + [0]*(m-1)

	for i in range(n-1):
		rabbits = [sum(rabbits[1:])] + rabbits[:-1]

	return sum(rabbits)

def main():
	n = 99
	m = 18
	print fib(n, m)

if __name__ == '__main__':
    main()