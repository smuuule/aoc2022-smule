import sys

win = {'R':'S', 'P':'R', 'S':'P'}
lose = {'S':'R', 'R':'P', 'P':'S'}
lookup = {'A':'R', 'B':'P', 'C':'S',
		  'X':'R', 'Y':'P', 'Z':'S'}

def translate(file: str) -> str:
	s: str = file.read()
	for k, v in lookup.items():
		s = s.replace(k, v)
	
	return s

def calcScore(foe: str, player: str) -> int:
	score: int = 0

	match player:
		case 'R':
			score += 1
		case 'P':
			score += 2
		case 'S':
			score += 3

	if player == foe:
		score += 3
	elif win[foe] != player: 
		score += 6
	else:
		pass

	return score

def partone(file) -> int:

	total: int = 0

	for line in translate(file).splitlines():
		a, b = line.split()
		total += calcScore(a, b)

	return total


def parttwo(file) -> int:

	total: int = 0

	for line in translate(file).splitlines():
		a, b = line.split()
		print(b)
		match b:
			case 'R':
				total += calcScore(a, win[a])
			case 'P':
				total += calcScore(a, a)
			case 'S':
				total += calcScore(a, lose[a])

	return total

if __name__ == "__main__":
	file = open(sys.argv[1], "r")

	if sys.argv[2] == "1":
		print(partone(file))
	elif sys.argv[2] == "2":
		print(parttwo(file))