boolean = lambda a,b,op:{"conjunction": a and b,
                         "disjunction": a or b,
                         "implication": not(a) or b,
                         "exclusive": a ^ b,
                         "equivalence":  a == b}[op]

print(boolean('equivalence', 0, 0))
print(boolean('equivalence', 1, 0))
print(boolean('equivalence', 0, 1))
print(boolean('equivalence', 1, 1))

