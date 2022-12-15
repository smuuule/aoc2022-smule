import sys

def popaction(arr: list[list[str]], line: str):
    _, q, _, f, _, t = line.split(' ')

    for i in range(int(q)):
        arr[int(t)-1].append(arr[int(f)-1].pop())

def moveaction(arr: list[list[str]], line: str):
    _, q, _, f, _, t = line.split(' ')

    arr[int(t)-1] += arr[int(f)-1][-int(q):]
    for i in range(int(q)):
        arr[int(f)-1].pop()


def partone(file) -> str:
    arr = [
        ["L", "N", "W", "T", "D"],
        ["C", "P", "H"],
        ["W", "P", "H", "N", "D", "G", "M", "J"],
        ["C", "W", "S", "N", "T", "Q", "L"],
        ["P", "H", "C", "N"],
        ["T", "H", "N", "D", "M", "W", "Q", "B"],
        ["M", "B", "R", "J", "G", "S", "L"],
        ["Z", "N", "W", "G", "V", "B", "R", "T"],
        ["W", "G", "D", "N", "P", "L"]
    ]

    for line in file.readlines():
        popaction(arr, line)
    
    result = ""
    for i in arr:
        result += i[-1]

    return result


def parttwo(file) -> str:

    arr = [
        ["L", "N", "W", "T", "D"],
        ["C", "P", "H"],
        ["W", "P", "H", "N", "D", "G", "M", "J"],
        ["C", "W", "S", "N", "T", "Q", "L"],
        ["P", "H", "C", "N"],
        ["T", "H", "N", "D", "M", "W", "Q", "B"],
        ["M", "B", "R", "J", "G", "S", "L"],
        ["Z", "N", "W", "G", "V", "B", "R", "T"],
        ["W", "G", "D", "N", "P", "L"]
    ]

    for line in file.readlines():
        moveaction(arr, line)

    result = ""
    for i in arr:
        result += i[-1]

    return result

if __name__ == "__main__":
	file = open(sys.argv[1], "r")

	if sys.argv[2] == "1":
		print(partone(file))
	elif sys.argv[2] == "2":
		print(parttwo(file))