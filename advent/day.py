from __future__ import annotations
from typing import Callable, Final
from types import ModuleType
from os.path import join


type PartFunction = Callable[[str], any]


INPUT_FILE_NAMES: Final = ("test", "input")


class Day:
	from typing import TYPE_CHECKING
	if TYPE_CHECKING: from .year import Year


	def __init__(self, number: int, year: Year) -> None:
		self.number = number
		self.year = year

		self._inputs: dict[str, str] = None
		self._solution_module: ModuleType = None
		self._parts: dict[int, PartFunction] = None

	@property
	def module_name(self) -> str:
		return f"day{self.number}"

	@property
	def rel_path(self) -> str:
		return join(self.year.rel_path, self.module_name)

	@property
	def abs_path(self) -> str:
		return join(self.year.abs_path, self.module_name)

	def get_inputs(self) -> dict[str, str]:
		if self._inputs is None:
			from os import scandir

			self._inputs = {}
			for entry in scandir(self.abs_path):
				if entry.is_dir(): continue

				name = entry.name
				if not name.endswith(".txt") and "." in name: continue

				name = name.removesuffix(".txt")
				from string import digits
				if name.rstrip(digits) not in INPUT_FILE_NAMES: continue

				with open(entry.path) as file:
					if not file.readable: continue
					self._inputs[name] = file.read()
		return self._inputs

	def get_solution_module(self) -> ModuleType:
		if self._solution_module is None:
			from importlib import import_module
			self._solution_module = import_module(
				f"{self.year.module_name}.{self.module_name}.solution"
			)
		return self._solution_module

	def get_parts(self) -> dict[int, PartFunction]:
		if self._parts is None:
			mod = self.get_solution_module()
			self._parts = {
				int(attr[4:]): getattr(mod, attr) for attr in dir(mod)
				if attr.startswith("part") and attr[4:].isdigit()
			}
		return self._parts
