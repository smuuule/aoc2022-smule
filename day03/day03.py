import sys

def itemPrio(item: str) -> int:
    if 97 <= ord(item) <= 122:
        return ord(item) - 96
    elif 65 <= ord(item) <= 90:
        return ord(item) - 38
    else:
        raise ValueError

def findCommon(a: str, b: str) -> str:
    
    commons: list[str] = []

    for item1 in a:
        for item2 in b:
            if item1 == item2:
                commons.append(item1)
    
    return commons

def partone(file) -> int:
    total: int = 0

    for sack in file.readlines():
        l: int = len(sack)//2 # mid index of rucksack
        a, b = sack[:l], sack[l:]
        common: str = findCommon(a, b)[0]
        print(common)
        total += itemPrio(common)

    return total

def parttwo(file) -> int:
    c: int = 0
    s: str = file.readlines()
    total: int = 0

    for i, sack in enumerate(s):
        if c == 0:
            for common in findCommon(s[i], s[i+1]):
                    total += itemPrio(common)
                    break
        c = (c + 1) % 3


    return total

if __name__ == "__main__":
	file = open(sys.argv[1], "r")

	if sys.argv[2] == "1":
		print(partone(file))
	elif sys.argv[2] == "2":
		print(parttwo(file))