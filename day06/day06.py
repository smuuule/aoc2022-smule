import sys

def containsDifferent(str: str) -> bool:
    for i, val1 in enumerate(str):
        for j, val2 in enumerate(str):
            if i == j:
                continue
            if val1 == val2:
                return False

    return True

def partone(file) -> int:

    msg: str = file.readlines()[0]

    for i, val in enumerate(msg):
        if containsDifferent(msg[i:i+4]):
            return i+4

def parttwo(file) -> int:

    msg: str = file.readlines()[0]

    for i, val in enumerate(msg):
        if containsDifferent(msg[i:i+14]):
            return i+14

if __name__ == "__main__":
	file = open(sys.argv[1], "r")

	if sys.argv[2] == "1":
		print(partone(file))
	elif sys.argv[2] == "2":
		print(parttwo(file))