from pykeen import krb_traceback, prolog

# Define the Prolog rules
prolog.load("""
    sum_list([], 0).
    sum_list([H|T], Sum) :-
        sum_list(T, TailSum),
        Sum is H + TailSum.
""")

# Define a function to calculate the sum using the Prolog code
def sum_list_elements(input_list):
    answer = prolog.call_query("sum_list", input_list, prolog.Variable("Sum"))
    return answer["Sum"]

# Testing the function
example_list = [1, 2, 3, 4, 5]
print("The sum of elements in the list:", sum_list_elements(example_list))
