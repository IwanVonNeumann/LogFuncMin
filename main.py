from log_utils import get_true_inputs
from matrix_coverage import get_implicant_matrix, print_implicant_matrix, list_all_combinations
from simple_implicants import list_simple_implicants

func_output_code = [1, 0, 1, 0, 1, 1, 0, 0]
print(func_output_code)

true_inputs = get_true_inputs(func_output_code)
print(true_inputs)

simple_implicants = list_simple_implicants(true_inputs)
print(simple_implicants)

implicant_matrix = get_implicant_matrix(simple_implicants, true_inputs)

print_implicant_matrix(simple_implicants, true_inputs, implicant_matrix)

print(list_all_combinations(simple_implicants))
