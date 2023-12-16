def is_symbol_nearby(search_line: int, search_col: int, lines: list[str]) -> bool:
	for line in [search_line - 1, search_line, search_line + 1]:
		if line not in range(len(lines)): continue
		for col in [search_col - 1, search_col, search_col + 1]:
			if col not in range(len(lines[line])): continue
			c = lines[line][col]
			if c.isdigit() or c == ".": continue
			return True

	return False


def part1(input: str) -> int:
	lines: list[str] = input.splitlines()
	line_range = range(len(lines))
	col_range = range(len(lines[0]))
	sum: int = 0

	for line in line_range:
		num_string: str = ""
		is_part_num: bool = False

		for col in col_range:
			c = lines[line][col]

			if c.isdigit():
				num_string += c
				is_part_num = is_part_num or is_symbol_nearby(line, col, lines)
			elif num_string != "":
				if is_part_num:
					sum += int(num_string)
					is_part_num = False
				num_string = ""

		if num_string != "" and is_part_num: sum += int(num_string)

	return sum
