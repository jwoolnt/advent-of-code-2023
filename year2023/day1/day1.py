def part1(input: str) -> int:
	search = "123456789"
	sum: int = 0

	for line in input.splitlines():
		first_dict = {line.find(item): item for item in search if line.find(item) != -1}
		last_dict = {line.rfind(item): item for item in search if line.rfind(item) != -1}

		first = first_dict[min(first_dict.keys())]
		last = last_dict[max(last_dict.keys())]

		sum += int(first + last)

	return sum


def part2(input: str) -> int:
	word_to_num_string = {
		"one":"1",
		"two":"2",
		"three":"3",
		"four":"4",
		"five":"5",
		"six":"6",
		"seven":"7",
		"eight":"8",
		"nine":"9"
	}
	search = list(word_to_num_string.keys())
	search.extend(word_to_num_string.values())
	sum: int = 0

	for line in input.splitlines():
		first_dict = {line.find(item): item for item in search if line.find(item) != -1}
		last_dict = {line.rfind(item): item for item in search if line.rfind(item) != -1}

		first = first_dict[min(first_dict.keys())]
		last = last_dict[max(last_dict.keys())]

		first = word_to_num_string[first] if first in word_to_num_string else first
		last = word_to_num_string[last] if last in word_to_num_string else last

		sum += int(first + last)

	return sum
