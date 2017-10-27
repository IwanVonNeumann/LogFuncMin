import math
import random


def get_func_order(output_number):
    order = math.log(output_number, 2)
    if order.is_integer():
        return int(order)
    raise ValueError("Logical function output number has to be an integer power of 2")


def gen_inputs(order):
    binary_format = "0" + str(order) + "b"
    return [format(i, binary_format) for i in range(2 ** order)]


def get_truth_table(outputs):
    order = get_func_order(len(outputs))
    inputs = gen_inputs(order)
    return list(zip(inputs, outputs))


def get_true_inputs(output):
    truth_table = get_truth_table(output)
    return [x[0] for x in truth_table if x[1] == 1]


def generate_func_output(order, threshold=0.5):
    return [bernoulli_random(threshold) for i in range(2 ** order)]


def bernoulli_random(p):
    return 1 if random.random() < p else 0
