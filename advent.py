from os import scandir
from types import ModuleType
from typing import Callable


years: list[int] = [int(entry.name[4:]) for entry in scandir() if entry.is_dir() and entry.name.startswith("year")]
days: dict[int, list[int]] = {
	year: [int(entry.name[3:-3]) for entry in scandir(f"year{year}") if entry.is_file() and entry.name.startswith("day")]
	for year in years
}

latest_year: int = years[-1]
latest_day: Callable[[int], int] = lambda year: days[year][-1]


class Solution:
	def fire(day: int = latest_day(latest_year), year: int = latest_year, **kwargs):
		"Runs the solution for a given day and year."
		if year not in years: raise IndexError(f"Given invalid argument for year '{year}'")
		if day not in days[year]: raise IndexError(f"Given invalid argument for day '{day}'")
		Solution(day, year).run(**kwargs)


	def __init__(self, day: int, year: int) -> None:
		self.day: int = day
		self.year: int = year

		self._module: ModuleType = None
		self._parts: list[str] = None
		self._inputs: dict[str, str] = None

	def get_module(self) -> ModuleType:
		if self._module is None:
			from importlib import import_module

			self._module = import_module(f"year{self.year}.day{self.day}")
		return self._module

	def get_parts(self) -> list[str]:
		if self._parts is None:
			self._parts = [name for name in dir(self.get_module()) if name.startswith("part")]
		return self._parts

	def get_input_folder_path(self) -> str:
		from os.path import join
		from os import getcwd

		return join(getcwd(), f"year{self.year}", "inputs", f"day{self.day}")

	def get_inputs(self) -> dict[str, str]:
		if self._inputs is None:
			from os import scandir

			self._inputs = {}
			for entry in scandir(self.get_input_folder_path()):
				with open(entry.path) as file:
					input_type = entry.name[:-4] if entry.name.endswith(".txt") else entry.name
					self._inputs[input_type] = file.read()

		return self._inputs


	def run(self, *, part: int = None, input: str = None) -> None:
		print(f"\nyear{self.year}/day{self.day}.py:\n\n")

		mod: ModuleType = self.get_module()
		solution_inputs: dict[str, str] = self.get_inputs()
		if input is not None: solution_inputs["input"] = input

		for part_str in self.get_parts():
			part_num: str = part_str[4:]
			if part is not None and part != int(part_num): continue
			part_func: Callable[[str], any] = getattr(mod, part_str)
			part_run: Callable[[str], None] = lambda input_type: print(
				f"\t{input_type} -> {part_func(solution_inputs[input_type])}\n"
			)

			print(f"Part {part_num}:")

			for allowed_input in ["input", f"test{part_num}", part_str, "test", "main"]:
				if allowed_input in solution_inputs:
					part_run(allowed_input)

		print("\nComplete!")
