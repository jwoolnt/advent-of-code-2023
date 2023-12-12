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


def day1(input: str) -> None:
	sum: int = 0

	for line in input.splitlines():
		first_dict = {line.find(item): item for item in search if line.find(item) != -1}
		last_dict = {line.rfind(item): item for item in search if line.rfind(item) != -1}

		first = first_dict[min(first_dict.keys())]
		last = last_dict[max(last_dict.keys())]

		first = first if first in word_to_num_string.values() else word_to_num_string[first]
		last = last if last in word_to_num_string.values() else word_to_num_string[last]

		sum += int(first + last)

	print(sum)


day1("""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""")

day1("""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""")