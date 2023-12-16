def setup(input: str) -> tuple[list[int], list[int]]:
	win_nums: list[int] = []
	our_nums: list[int] = []

	for line in input.splitlines():
		[_, card_data] = line.split(":")
		[win_str, our_str] = card_data.split("|")
		win_nums.append([int(num_str) for num_str in win_str.split()])
		our_nums.append([int(num_str) for num_str in our_str.split()])

	return (win_nums, our_nums)


def part1(input: str):
	(win_nums, our_nums) = setup(input)
	sum: int = 0

	for card_num in range(len(win_nums)):
		card_wins: int = 0

		for num in our_nums[card_num]:
			card_wins += num in win_nums[card_num]

		sum += 2 ** (card_wins - 1) if card_wins > 0 else 0

	return sum