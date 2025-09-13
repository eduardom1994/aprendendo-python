dados = [
    "   João da Silva   \n",
    "\tMaria Oliveira   ",
    "  Carlos Souza***",
    "***Ana Paula   ",
    "\n   Pedro Santos   \t"
]


for v in dados:
    print(v.strip(" \n\t*"))