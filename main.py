from Assembler_II.Statement import Statement
from Assembler_II.StatementInstance import StatementInstance
from Assembler_II.Theorem import Theorem
from Assembler_II.Theodem import Theodem
from Assembler_II.Prover import Prover

with open('lol.json', 'r') as file:
	Theodem.load_file(file)

Prover("loltheorem")