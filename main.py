from Assembler.Property import PropertyInstance, DeclaredProperties
from Assembler.Theodem import Theodem
from Assembler.Variables import Variable
from Assembler.macros import encode_json

with open('lol.json', 'r') as file:
	Theodem.init(file)

prop = DeclaredProperties.getInstance('equalsto', {'A':"B"})
prop1 = DeclaredProperties.getInstance('equalsto', {'A':"A"})
prop2 = DeclaredProperties.getInstance('equalsto', {'A':"A"})
lol = Variable([prop, prop1])
klar = Variable([prop, prop2],"klar")

print(lol == klar)

print("\n\n")

Theodem.prove("loltheorem")