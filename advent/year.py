class Year:
	TEST_YEAR_ID = "TEST"


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
	def year_str(self) -> str:
		return f"year{self.number}"

	@property
	def rel_path(self) -> str:
		return str(self.year_str) if self.number != 0 else Year.TEST_YEAR_ID

	@property
	def abs_path(self) -> str:
		from os.path import join
		from os import getcwd
		return join(getcwd(), self.rel_path)