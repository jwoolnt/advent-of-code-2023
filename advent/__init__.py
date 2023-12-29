from os import scandir

from .year import Year, TEST_YEAR_ID


type AdventTree = dict[int, Year]


tree: AdventTree = {}

for entry in scandir():
	if entry.is_file() or not entry.name.startswith("year"): continue

	year_id = entry.name[4:]
	year_num: int

	if year_id.isdigit(): year_num = int(year_id)
	elif year_id is TEST_YEAR_ID: year_num = 0
	else: continue

	tree[year_num] = Year(year_num)
