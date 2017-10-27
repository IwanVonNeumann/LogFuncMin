import collections


def group_terms(terms):
    grouped = collections.defaultdict(list)
    weights = [x.count("1") for x in terms]
    for weight, term in zip(weights, terms):
        grouped[weight].append(term)
    sorted_keys = sorted(grouped.keys())
    return [grouped[k] for k in sorted_keys]


def combine_groups(grouped_terms):
    n = len(grouped_terms)
    used_terms = set()
    combined_terms = set()
    for i in range(n - 1):
        group_1 = grouped_terms[i]
        group_2 = grouped_terms[i + 1]
        for x in group_1:
            for y in group_2:
                if is_possible_to_combine(x, y):
                    combined_terms.add(combine_terms(x, y))
                    used_terms.update([x, y])
    flat_terms = [term for group in grouped_terms for term in group]
    unused_terms = [term for term in flat_terms if term not in used_terms]
    return list(combined_terms), unused_terms


def is_possible_to_combine(x, y):
    return differences_count(x, y) == 1


def differences_count(x, y):
    return sum(1 for a, b in zip(x, y) if a != b)


def combine_terms(x, y):
    return "".join([a if a == b else "-" for a, b in zip(x, y)])


def list_simple_implicants(terms):
    simple_implicants = []
    grouped_terms = group_terms(terms)
    while True:
        combined_terms, unused_terms = combine_groups(grouped_terms)
        simple_implicants.extend(unused_terms)
        if len(combined_terms) == 0:
            break
        grouped_terms = group_terms(combined_terms)
    return simple_implicants
