from os.path import join


class Day:
	from typing import TYPE_CHECKING
	if TYPE_CHECKING: from .year import Year

	def __init__(self, number: int, year: Year) -> None:
		self.number = number
		self.year = year

	@property
	def day_str(self) -> str:
		return f"day{self.number}"

	@property
	def rel_path(self) -> str:
		return join(self.year.rel_path, self.day_str)

	@property
	def abs_path(self) -> str:
		return join(self.year.abs_path, self.day_str)
