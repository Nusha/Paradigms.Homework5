import pytholog as pl

list_kb = pl.KnowledgeBase("list")
list_kb.add_kn(["list_sum([Item], 0)"])
list_kb.add_kn(["list_sum2([Item2|Tail], Total) :- Temp is Item1+Item2, list_sum([Temp|Tail], Total)"])
list_kb.add_kn(["list_sum([Item|[]], Item)"])

item = [1,2,3]
result = list_kb.query(pl.Expr("list_sum([qwerty], S)"))
print(result)
