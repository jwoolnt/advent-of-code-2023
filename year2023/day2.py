def setup(input: str) -> dict[str, dict[str, int]]:
	data: dict[str, dict[str, int]] = {}

	for game in input.splitlines():
		[game_id, game_data] = game.split(":")
		game_num = game_id.split(" ")[-1]
		data[game_num] = {
			"red": 0,
			"green": 0,
			"blue": 0
		}

		for set_data in game_data.split(";"):
			for datapoint in set_data.split(", "):
				[*_, num, color] = datapoint.split(" ")
				num = int(num)

				if data[game_num][color] < num:
					data[game_num][color] = num

	return data

cube_amounts = {
	"red": 12,
	"green": 13,
	"blue": 14
}


def part1(input: str):
	data: dict[str, dict[str, int]] = setup(input)
	sum: int = 0

	for game_num in data:
		possible: bool = True

		for color in data[game_num]:
			if cube_amounts[color] < data[game_num][color]:
				possible = False
				break

		if possible:
			sum += int(game_num)

	return sum


def part2(input: str):
	data: dict[str, dict[str, int]] = setup(input)
	sum: int = 0

	for game_num in data:
		power: int = 1

		for color in data[game_num]:
			power *= data[game_num][color]

		sum += power

	return sum
