from log_utils import get_true_inputs
from matrix_coverage import get_implicant_matrix, print_implicant_matrix, solve_by_min_length, solve_by_min_rank
from simple_implicants import list_simple_implicants


def solve_with_nice_output(func_output_code, log=False):
    print("Function outputs code:")
    print(func_output_code)
    print()

    true_inputs = get_true_inputs(func_output_code)
    if log:
        print("True input sets ({}):".format(len(true_inputs)))
        print(true_inputs)
        print()

    simple_implicants = list_simple_implicants(true_inputs)
    if log:
        print("Simple implicants ({}):".format(len(simple_implicants)))
        print(simple_implicants)
        print()

    implicant_matrix = get_implicant_matrix(simple_implicants, true_inputs)
    if log:
        print("Implicant matrix:")
        print_implicant_matrix(simple_implicants, true_inputs, implicant_matrix)
        print()

    min_length_coverages = solve_by_min_length(simple_implicants, true_inputs, log=log)
    min_rank_coverages = solve_by_min_rank(simple_implicants, true_inputs, log=log)

    return min_length_coverages, min_rank_coverages
