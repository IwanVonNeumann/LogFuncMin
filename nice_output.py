from log_utils import get_true_inputs
from matrix_coverage import get_implicant_matrix, print_implicant_matrix, solve_by_min_length, solve_by_min_rank
from simple_implicants import list_simple_implicants


def solve_with_nice_output(func_output_code):
    print("Function outputs code:")
    print(func_output_code)
    print()

    true_inputs = get_true_inputs(func_output_code)
    print("True input sets ({}):".format(len(true_inputs)))
    print(true_inputs)
    print()

    simple_implicants = list_simple_implicants(true_inputs)
    print("Simple implicants ({}):".format(len(simple_implicants)))
    print(simple_implicants)
    print()

    print("Implicant matrix:")
    implicant_matrix = get_implicant_matrix(simple_implicants, true_inputs)
    print_implicant_matrix(simple_implicants, true_inputs, implicant_matrix)
    print()

    solve_by_min_length(simple_implicants, true_inputs, log=True)

    solve_by_min_rank(simple_implicants, true_inputs, log=True)
