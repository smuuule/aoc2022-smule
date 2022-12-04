import sys

def parse(input: str) -> list[int]:
    input: list[str] = input.strip().split(',')
    splitted: list[int] = []
    for elf in input:
        splitted += elf.split('-')

    for i, n in enumerate(splitted):
        splitted[i] = int(splitted[i])
        
    return splitted

def partone(file) -> int:
    total: int = 0

    for line in file.readlines():
        parsed: list[int] = parse(line)
        if parsed[0] <= parsed[2] and parsed[1] >= parsed[3]:
            total += 1
        elif parsed[0] >= parsed[2] and parsed[1] <= parsed[3]:
            total += 1

    return total

def parttwo(file) -> int:
    total: int = 0
    
    for line in file.readlines():
        parsed: list[int] = parse(line)
        if parsed[1] >= parsed[2] and parsed[0] <= parsed[3]:
            total += 1

    return total

if __name__ == "__main__":
	file = open(sys.argv[1], "r")

	if sys.argv[2] == "1":
		print(partone(file))
	elif sys.argv[2] == "2":
		print(parttwo(file))