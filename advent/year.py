from typing import Final


TEST_YEAR_ID: Final = "TEST"


class Year:
	def __init__(self, number: int) -> None:
		from os import scandir
		from .day import Day

		self.number = number
		self.days: list[Day] = []

		for entry in scandir(self.abs_path):
			if entry.is_file() or not entry.name.startswith("day"): continue

			day_id = entry.name[3:].removesuffix(".py")
			if day_id.isdigit(): self.days.append(Day(int(day_id), self))

	@property
	def module_name(self) -> str:
		return f"year{self.number if self.number != 0 else TEST_YEAR_ID}"

	@property
	def rel_path(self) -> str:
		return self.module_name

	@property
	def abs_path(self) -> str:
		from os.path import join
		from os import getcwd
		return join(getcwd(), self.rel_path)