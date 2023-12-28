from typing import Callable


def setup1(input: str) -> list[tuple[int, int]]:
	[time_str, distance_str] = input.splitlines()
	[_, time_data] = time_str.split(":")
	times: list[int] = [int(num_str) for num_str in time_data.split()]
	[_, distance_data] = distance_str.split(":")
	distances: list[int] = [int(num_str) for num_str in distance_data.split()]
	return [(times[i], distances[i]) for i in range(len(times))]

def winning_options(race: tuple[int, int]) -> range:
	TIME: int = race[0]
	time_range: range = range(1, TIME)
	start: int = 1

	for t in time_range:
		if t * (TIME - t) <= race[1]: continue
		start = t
		break

	for t in reversed(time_range):
		if t * (TIME - t) <= race[1]: continue
		return t - start + 1



def part1(input: str) -> int:
	races: list[tuple[int, int]] = setup1(input)
	prod: int = 1

	for race in races:
		prod *= winning_options(race)

	return prod


def setup2(input: str) -> tuple[int, int]:
	[time_line, distance_line] = input.splitlines()
	[_, time_data] = time_line.split(":")
	time_str: str = ""

	for num_str in time_data.split():
		time_str += num_str

	[_, distance_data] = distance_line.split(":")
	distance_str: str = ""

	for num_str in distance_data.split():
		distance_str += num_str

	return (int(time_str), int(distance_str))


part2: Callable[[str], int] = lambda input: winning_options(setup2(input))
