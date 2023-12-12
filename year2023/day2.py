cube_amounts = {
	"red": 12,
	"green": 13,
	"blue": 14
}


def day2(input: str) -> None:
	data: dict[str, dict[str, int]] = {}

	for game in input.splitlines():
		[game_id, game_data] = game.split(":")
		num_string_id = game_id.split(" ")[-1]

		data[num_string_id] = {
			"red": 0,
			"green": 0,
			"blue": 0
		}

		for set_data in game_data.split(";"):
			for datapoint in set_data.split(", "):
				[*_, num, color] = datapoint.split(" ")
				num = int(num)

				if data[num_string_id][color] < num:
					data[num_string_id][color] = num


	# Part 1
	sum = 0

	for game_id in data:
		possible = True

		for color in data[game_id]:
			if cube_amounts[color] < data[game_id][color]:
				possible = False
				break

		if possible:
			sum += int(game_id)

	print("Part 1:", sum)


	# Part 2
	sum = 0

	for game_id in data:
		power = 1

		for color in data[game_id]:
			power *= data[game_id][color]

		sum += power

	print("Part 2:", sum)



day2("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""")
