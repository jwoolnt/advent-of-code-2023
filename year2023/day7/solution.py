from typing import Callable


type Hand = tuple[str, int]

def setup(input: str) -> list[Hand]:
	hands: list[Hand] = []

	for hand_str in input.splitlines():
		[cards, bid] = hand_str.split()
		hands.append((cards, int(bid)))

	return hands

def get_hand_type(char_dict: dict[str, int]) -> str:
	match len(char_dict):
		case 1:
			return "7"
		case 2:
			first: int = char_dict.popitem()[1]
			return "6" if first == 1 or first == 4 else "5"
		case 3:
			return "4" if 2 not in list(char_dict.values()) else "3"
		case 4:
			return "2"
		case 5:
			return "1"


def key1(hand: Hand) -> int:
	key_str: str = ""
	char_dict: dict[str, int] = {}

	for c in hand[0]:
		key_str += str("23456789TJQKA".find(c)).zfill(2)
		char_dict[c] = char_dict[c] + 1 if c in char_dict else 1

	key_str = get_hand_type(char_dict) + key_str
	return int(key_str)


def part1(input: str, key: Callable[[Hand], int] = key1) -> int:
	hands: list[Hand] = setup(input)
	hands.sort(key=key)
	sum: int = 0

	for i in range(len(hands)):
		sum += hands[i][1] * (i + 1)

	return sum


def key2(hand: Hand) -> int:
	card_str: str = hand[0]
	key_str: str = ""
	char_dict: dict[str, int] = {}

	for c in card_str:
		key_str += str("J23456789TQKA".find(c)).zfill(2)
		if c != "J": char_dict[c] = char_dict[c] + 1 if c in char_dict else 1

	match (len(char_dict), card_str.count("J")):
		# No J
		case (_, 0):
			key_str += get_hand_type(char_dict)
		# 5 J or 1 Non-J Type: J J J J J or J J J J 1, J J J 1 1, J J 1 1 1, J 1 1 1 1
		case (0, 5), (1, _):
			key_str += "7"
		# 2 Non-J Types and 1 J: J 1 1 2 2
		case (2, 1):
			key_str += "5"
		# 2 Non-J Types and # J: J J J 1 2 or J J 1 1 2 or J 1 1 1 2
		case (2, _):
			key_str += "6"
		# 3 Non-J Types and # J: J J 1 2 3 or J 1 1 2 3
		case (3, _):
			key_str += "4"
		# 4 Non-J Types and 1 J: J 1 2 3 4
		case (4, 1):
			key_str += "2"

	return int(key_str[-1] + key_str[:-1])


part2: Callable[[str], int] = lambda input: part1(input, key2)
