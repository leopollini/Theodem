import json
from Assembler.Theodem import Theodem


with open('lol.json', 'r') as file:
	Theodem.init(file)
