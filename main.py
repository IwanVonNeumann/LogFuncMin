from log_utils import generate_func_output
from nice_output import solve_with_nice_output

# func_output_code = [1, 0, 1, 0, 1, 1, 0, 1]
func_output_code = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1]
# func_output_code = generate_func_output(4, threshold=0.8)

solve_with_nice_output(func_output_code, log=True)
