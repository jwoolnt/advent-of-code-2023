def setup(input: str) -> tuple[list[int], list[dict[range, int]]]:
	[seed_line, *maps] = input.split("\n\n")

	[_, seed_data] = seed_line.split(":")
	seeds: list[int] = [int(num_str) for num_str in seed_data.split()]

	almanac: list[dict[int, int]] = []

	for map in maps:
		[_, map_data] = map.split(" map:\n")
		map_dict: dict[range, int] = {}

		for line in map_data.splitlines():
			[destination, source, range_len] = [int(num_str) for num_str in line.split()]
			map_dict[range(source, source + range_len)] = destination - source

		almanac.append(map_dict)

	return (seeds, almanac)


def part1(input: str) -> int:
	(seeds, almanac) = setup(input)
	values: list[int] = seeds

	for conv in almanac:
		for i in range(len(values)):
			conv_offset: int = 0

			for conv_range in conv:
				if values[i] in conv_range:
					conv_offset = conv[conv_range]
					break

			values[i] = values[i] + conv_offset

	return min(values)
