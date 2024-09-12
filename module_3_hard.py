data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    sum_numbers = 0
    sum_strings = 0


    def counting(symb):
        nonlocal sum_numbers, sum_strings
        if isinstance(symb, list) or isinstance(symb, tuple) or isinstance(symb, set):
            for item in symb:
                counting(item)
        elif isinstance(symb, dict):
            for value in symb.values():
                counting(value)
            for key in symb.keys():
                counting(key)
        elif isinstance(symb, int) or isinstance(symb, str):
            if isinstance(symb, int):
                sum_numbers += symb
            elif isinstance(symb, str):
                sum_strings += len(symb)

    counting(data_structure)
    return sum_numbers + sum_strings

result = calculate_structure_sum(data_structure)
print(result)

