import pyswip

# Создаем новый экземпляр интерпретатора Prolog
prolog = pyswip.Prolog

# Загружаем правило sum_list
prolog.assertz("sum_list([], 0).")
prolog.assertz("sum_list([H|T], Sum) :- sum_list(T, Rest), Sum is H + Rest.")

# Вызываем sum_list с заданным списком
list_values = [1,2,3,4,5]
list_term = "[" + ",".join(map(str, list_values)) + "]" # преобразуем список в строку формата "[1,2,3,4,5]"
sum_query = "sum_list({}, Sum)".format(list_term)
for solution in prolog.query(sum_query):
    print(solution["Sum"])
