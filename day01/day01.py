import sys

def get_inventory(file) -> list[int]:

	count: int = 0
	inventory: list[int] = []

	for line in file.readlines():
		if line != "\n":
			count += int(line)
		else:
			inventory.append(count)
			count = 0
	inventory.sort()

	return inventory

def partone(file) -> int:

	return get_inventory(file)[-1]

def parttwo(file) -> int:

	return sum(get_inventory(file)[-3:])

if __name__ == "__main__":
	file = open(sys.argv[1], "r")

	if sys.argv[2] == "1":
		print(partone(file))
	elif sys.argv[2] == "2":
		print(parttwo(file))