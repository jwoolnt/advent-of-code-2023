from types import ModuleType
from typing import Callable


class Solution:
	def __init__(self, year: int, day: int) -> None:
		self.year: int = year
		self.day: int = day

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

		return join(getcwd(), f"year{self.year}", f"day{self.day}")

	def get_inputs(self) -> dict[str, str]:
		if self._inputs is None:
			from os import scandir

			self._inputs = {}
			for entry in scandir(self.get_input_folder_path()):
				with open(entry.path) as file:
					self._inputs[entry.name[:-4]] = file.read()
		return self._inputs


	def run(self) -> None:
		print(f"Running Solution for Year {self.year} Day {self.day}...", "\n")

		mod = self.get_module()
		inputs = self.get_inputs()

		for part in self.get_parts():
			print(part.capitalize() + ":")

			part_func: Callable[[str], any] = getattr(mod, part)
			part_run: Callable[[str], None] = lambda input_name: print(f"{input_name}.txt -> {part_func(inputs[input_name])}")

			if part in inputs:
				part_run(part)
			part_run("main")

			print("\b")

		print("Complete!")