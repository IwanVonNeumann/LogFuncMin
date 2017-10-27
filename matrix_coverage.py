import itertools

import collections


def get_implicant_matrix(simple_implicants, true_inputs):
    return [[1 if implicant_covers_input_set(impl, inp) else 0 for inp in true_inputs] for impl in simple_implicants]


def implicant_covers_input_set(imlicant, input_set):
    uncovered_variables_count = sum(1 for a, b in zip(imlicant, input_set) if a != "-" and a != b)
    return uncovered_variables_count == 0


def print_implicant_matrix(simple_implicants, true_inputs, implicant_matrix):
    print("\t" + "\t".join(true_inputs))
    str_matrix = int_matrix_to_str_matrix(implicant_matrix)
    for i in range(len(simple_implicants)):
        print(simple_implicants[i] + "\t" + "\t".join(str_matrix[i]))


def int_matrix_to_str_matrix(matrix):
    return [[str(x) for x in row] for row in matrix]


def list_all_coverages(simple_implicants, true_inputs):
    all_implicant_combinations = list_all_combinations(simple_implicants)
    return [c for c in all_implicant_combinations if implicant_combination_covers_all_true_inputs(c, true_inputs)]


def list_all_combinations(items):
    all_combinations = [list(itertools.combinations(items, i + 1)) for i in range(len(items))]
    return flat_list(all_combinations)


def flat_list(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def implicant_combination_covers_all_true_inputs(implicant_combination, true_inputs):
    covered_input_sets = set()
    for implicant in implicant_combination:
        for input_set in true_inputs:
            if implicant_covers_input_set(implicant, input_set):
                covered_input_sets.add(input_set)
    uncovered_input_sets = set(true_inputs).difference(covered_input_sets)
    return len(uncovered_input_sets) == 0


def group_coverages_by_length(coverages):
    return group_coverages(coverages, criterion=len)


def find_coverages_with_min_length(coverages):
    return find_coverages_with_min_weight(coverages, criterion=len)


def group_coverages_by_rank(coverages):
    return group_coverages(coverages, criterion=rank_of_coverage)


def group_coverages(coverages, criterion):
    grouped = collections.defaultdict(list)
    weights = [criterion(c) for c in coverages]
    for weight, coverage in zip(weights, coverages):
        grouped[weight].append(coverage)
    return dict(grouped)


def rank_of_coverage(coverage):
    return sum(rank_of_term(term) for term in coverage)


def rank_of_term(term):
    return term.count("0") + term.count("1")


def find_coverages_with_min_rank(coverages):
    return find_coverages_with_min_weight(coverages, criterion=rank_of_coverage)


def find_coverages_with_min_weight(coverages, criterion):
    grouped_coverages = group_coverages(coverages, criterion=criterion)
    min_weight = min(grouped_coverages, key=grouped_coverages.get)
    return grouped_coverages[min_weight]


def solve_by_min_length(simple_implicants, true_inputs, log=False):
    coverages = list_all_coverages(simple_implicants, true_inputs)
    if log:
        print("All coverages:")
        for c in coverages:
            print(c)
        print()
        grouped_coverages = group_coverages_by_length(coverages)
        print("Grouped coverages:")
        for k in grouped_coverages:
            print("{}: {}".format(k, grouped_coverages[k]))
    min_length_coverages = find_coverages_with_min_length(coverages)
    if log:
        print()
        min_length = len(min_length_coverages[0])
        print("Min length coverages (length={}):".format(min_length))
        print(min_length_coverages)
        print()
    return min_length_coverages


def solve_by_min_rank(simple_implicants, true_inputs, log=False):
    coverages = list_all_coverages(simple_implicants, true_inputs)
    if log:
        print("All coverages:")
        for c in coverages:
            print(c)
        print()
        grouped_coverages = group_coverages_by_rank(coverages)
        print("Grouped coverages:")
        for k in grouped_coverages:
            print("{}: {}".format(k, grouped_coverages[k]))
    min_rank_coverages = find_coverages_with_min_rank(coverages)
    if log:
        print()
        min_rank = rank_of_coverage(min_rank_coverages[0])
        print("Min rank coverages (rank={}):".format(min_rank))
        print(min_rank_coverages)
        print()
    return min_rank_coverages
