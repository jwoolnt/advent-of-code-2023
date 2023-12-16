def setup(input: str) -> tuple[list[int], list[int]]:
	win_nums: list[int] = []
	our_nums: list[int] = []

	for line in input.splitlines():
		[_, card_data] = line.split(":")
		[win_str, our_str] = card_data.split("|")
		win_nums.append([int(num_str) for num_str in win_str.split()])
		our_nums.append([int(num_str) for num_str in our_str.split()])

	return (win_nums, our_nums)


def part1(input: str) -> int:
	(win_nums, our_nums) = setup(input)
	point_sum: int = 0

	for card_num in range(len(win_nums)):
		card_wins: int = sum([num in win_nums[card_num] for num in our_nums[card_num]])
		point_sum += 2 ** (card_wins - 1) if card_wins > 0 else 0

	return point_sum


def part2(input: str) -> int:
	(win_nums, our_nums) = setup(input)
	cards: list[int] = [1] * len(win_nums)

	for card_num in range(len(cards)):
		card_wins: int = sum([num in win_nums[card_num] for num in our_nums[card_num]])

		for i in range(card_num + 1, card_num + card_wins + 1):
			cards[i] += cards[card_num]

	return sum(cards)
