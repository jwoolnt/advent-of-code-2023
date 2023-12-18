type Hand = tuple[str, int]

def setup(input: str) -> list[Hand]:
	hands: list[Hand] = []

	for hand_str in input.splitlines():
		[cards, bid] = hand_str.split()
		hands.append((cards, int(bid)))

	return hands

def key(hand: Hand) -> int:
	key_str: str = ""
	char_dict: dict[str, int] = {}

	for c in hand[0]:
		key_str += str("23456789TJQKA".find(c)).zfill(2)
		char_dict[c] = char_dict[c] + 1 if c in char_dict else 1

	match len(char_dict):
		case 1:
			key_str += "7"
		case 2:
			first: int = char_dict.popitem()[1]
			key_str += "6" if first == 1 or first == 4 else "5"
		case 3:
			key_str += "4" if 2 not in list(char_dict.values()) else "3"
		case 4:
			key_str += "2"
		case 5:
			key_str += "1"

	return int(key_str[-1] + key_str[:-1])



def part1(input: str) -> int:
	hands: list[Hand] = setup(input)
	hands.sort(key=key)
	sum: int = 0

	for i in range(len(hands)):
		sum += hands[i][1] * (i + 1)

	return sum
