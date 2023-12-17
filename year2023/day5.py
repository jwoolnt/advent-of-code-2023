type Conversion = tuple[int, int, int]
type Map = list[Conversion]
type Almanac = list[Map]

def setup1(input: str) -> tuple[list[int], Almanac]:
	[seed_line, *map_strs] = input.split("\n\n")

	[_, seed_data] = seed_line.split(":")
	seeds: list[int] = [int(num_str) for num_str in seed_data.split()]

	almanac: Almanac = []

	for map_str in map_strs:
		[_, map_data] = map_str.split(" map:\n")
		almanac.append([
			[int(num_str) for num_str in line.split()] for line in map_data.splitlines()
		])

	return (seeds, almanac)


def part1(input: str) -> int:
	(seeds, almanac) = setup1(input)
	values: list[int] = seeds

	for map in almanac:
		for i in range(len(values)):
			conv_offset: int = 0

			for conv in map:
				if values[i] in range(conv[1], conv[1] + conv[2]):
					conv_offset = conv[0] - conv[1]
					break

			values[i] = values[i] + conv_offset

	return min(values)


type InputRange = tuple[int, int]

def setup2(input: str) -> tuple[list[InputRange], Almanac]:
	(seeds, almanac) = setup1(input)

	seed_ranges: list[InputRange] = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
	seed_ranges.sort(key=lambda seed_range: seed_range[0])

	for map in almanac:
		map.sort(key=lambda conv: conv[1])

	return (seed_ranges, almanac)

def adjust_ranges(input_ranges: list[InputRange], map: Map) -> list[InputRange]:
	new_ranges: list[InputRange] = []

	for input_range in input_ranges:
		py_range: range = range(input_range[0], sum(input_range))
		bounds: list[int] = [py_range.start]

		for conv in map:
			(_, start, conv_len) = conv
			end = start + conv_len

			if start in py_range: bounds.append(start)
			if end in py_range: bounds.append(end)

		bounds.append(py_range.stop)

		for i in range(1, len(bounds)):
			last: int = bounds[i - 1]
			new_ranges.append((last, bounds[i] - last))

	return new_ranges


def part1(input: str) -> int:
	(seed_ranges, almanac) = setup2(input)
	value_ranges: list[InputRange] = seed_ranges

	for map in almanac:
		value_ranges = adjust_ranges(value_ranges, map)

		for i in range(len(value_ranges)):
			conv_offset: int = 0

			for conv in map:
				if value_ranges[i][0] in range(conv[1], conv[1] + conv[2]):
					conv_offset = conv[0] - conv[1]
					break

			value_ranges[i] = (value_ranges[i][0] + conv_offset, value_ranges[i][1])

	return min(value_ranges, key=lambda value_range: value_range[0])[0]
