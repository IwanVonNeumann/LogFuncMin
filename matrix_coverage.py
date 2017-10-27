import itertools


def get_implicant_matrix(simple_implicants, true_inputs):
    return [[1 if covers(impl, inp) else 0 for inp in true_inputs] for impl in simple_implicants]


def covers(imlicant, input_set):
    uncovered_variables = sum(1 for a, b in zip(imlicant, input_set) if a != "-" and a != b)
    return uncovered_variables == 0


def print_implicant_matrix(simple_implicants, true_inputs, implicant_matrix):
    print("\t" + "\t".join(true_inputs))
    str_matrix = int_matrix_to_str_matrix(implicant_matrix)
    for i in range(len(simple_implicants)):
        print(simple_implicants[i] + "\t" + "\t".join(str_matrix[i]))


def int_matrix_to_str_matrix(matrix):
    return [[str(x) for x in row] for row in matrix]


def list_all_combinations(items):
    all_combinations = [list(itertools.combinations(items, i + 1)) for i in range(len(items))]
    return flat_list(all_combinations)


def flat_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]
