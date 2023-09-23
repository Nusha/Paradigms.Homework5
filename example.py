import pytholog as pl

friends_kb = pl.KnowledgeBase()
friends_kb([
    "to_sum([], 0)",
    "to_sum([Head | Tail], Sum) :- to_sum(Tail, TailSum), Sum is Head + TailSum",
    "massive([1, 2, 3, 4, 5])",
    "to_sum(massive, Sum)."
])

query_result = friends_kb.query(pl.Expr("to_sum(massive, Sum)"))

if query_result:
    print(query_result)
else:
    print("No")
