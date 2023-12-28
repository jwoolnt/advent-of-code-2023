from typing import Callable


search_range: Callable[[int], range] = lambda index: range(index - 1, index + 2)

def is_symbol_nearby(search_line: int, search_col: int, lines: list[str]) -> bool:
	for line in search_range(search_line):
		if line not in range(len(lines)): continue
		for col in search_range(search_col):
			if col not in range(len(lines[line])): continue
			c = lines[line][col]
			if c.isdigit() or c == ".": continue
			return True

	return False


def part1(input: str) -> int:
	lines: list[str] = input.splitlines()
	sum: int = 0

	for line in range(len(lines)):
		num_string: str = ""
		is_part_num: bool = False

		for col in range(len(lines[line])):
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


def setup2(input: str) -> tuple[list[list[int]], list[dict[range, str]]]:
	stars: list[int] = []
	numbers: list[range] = []

	for line in input.splitlines():
		from re import finditer
		stars.append([m.start() for m in finditer("[*]", line)])
		numbers.append({range(m.start(), m.end()):int(m.group()) for m in finditer("\d+", line)})

	return (stars, numbers)

def get_nearby_numbers(search_line: int, searc_col: int, numbers: list[dict[range, str]]) -> list[int]:
	nearby_numbers: list[int] = []

	for line in search_range(search_line):
		if line not in range(len(numbers)): continue
		for num_range in numbers[line]:
			for col in search_range(searc_col):
				if col in num_range:
					nearby_numbers.append(numbers[line][num_range])
					break

	return nearby_numbers


def part2(input: str) -> int:
	(input_stars, input_numbers) = setup2(input)
	sum: int = 0

	for line in range(len(input_stars)):
		for col in input_stars[line]:
			numbers = get_nearby_numbers(line, col, input_numbers)
			if len(numbers) == 2:
				sum += numbers[0] * numbers[1]

	return sum
