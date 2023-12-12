from os import scandir, path, getcwd
from importlib import import_module


cwd: str = getcwd()
advent_tree: dict[str, dict[str, list[str]]] = {}

year_folders: list[str] = [entry.name for entry in scandir() if entry.is_dir() and entry.name.startswith("year")]

for year_folder in year_folders:
	advent_tree[year_folder] = {}

	for entry in scandir(path.join(getcwd(), year_folder)):
		if entry.is_file() and entry.name.endswith(".py"):
			mod = import_module(f"{year_folder}.{entry.name[:-3]}")
			advent_tree[year_folder][entry.name] = [name for name in dir(mod) if name.startswith("part")]