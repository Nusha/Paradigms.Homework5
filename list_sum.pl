list_sum([], 0).

list_sum([Head | Tail], TotalSum) :-
    list_sum(Tail, Sum1),
    TotalSum is Head + Sum1.

list_sum([1, 2, 3, 4, 5, 6], Sum).
