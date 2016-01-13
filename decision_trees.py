from math import log


def gain(examples, attribute_test, truth_label):
    """Returns the gain of info after applying an attribute_test.

    Params:
        examples: a list of (example (dict), label) tuples.
        attribute_test: a callable that returns a boolean given an example.
        truth_label: any one of the two labels.
    Returns:
        A float representing the gain in information.
    """
    p, n = get_label_count(examples, truth_label)
    return info(p, n) - entropy(examples, attribute_test, truth_label)

def info(positive, negative):
    """Returns the information to be unpacked in the distribution.

    Params:
        positive: the number of examples with label == truth_label
        negative: the number of examples with label != truth_label
    Returns:
        A float representing information still packed in the sample.
    """
    if positive == 0 or negative == 0: return 0
    total = float(positive + negative)
    p_ratio = positive / total
    n_ratio = negative / total
    return - p_ratio * log(p_ratio, 2) - n_ratio * log(n_ratio, 2)

def entropy(examples, attribute_test, truth_label):
    """Returns the entropy after applying an attribute_test.

    Params:
        examples: a list of (example (dict), label) tuples.
        attribute_test: a callable that returns a boolean given an example.
        truth_label: any one of the two labels.
    Returns:
        A float representing the entropy of the sample after the attr split.
    """
    total = float(len(examples))
    true, false = apply_attribute(examples, attribute_test)
    p_t, n_t = get_label_count(true, truth_label)
    p_f, n_f = get_label_count(false, truth_label)
    t_ratio = (p_t + n_t) / total
    f_ratio = (p_f + n_f) / total
    return t_ratio * info(p_t, n_t) + f_ratio * info(p_f, n_f)


def get_label_count(examples, truth_label):
    """Returns the number of examples with label equal to each label."""
    p = len([sample for sample, label in examples if label == truth_label])
    n = len(examples) - p
    return p, n

def apply_attribute(examples, attribute_test):
    """Returns the examples split by attribute_test."""
    true = filter(attribute_test, examples)
    false = filter(lambda x: not attribute_test(x), examples)
    return true, false


if __name__ == '__main__':
    from sample_dataset import sample_dataset

    attributes = sample_dataset[0][0].keys()
    generate_attr_test = lambda attr: lambda x: x[0][attr]

    for attr in attributes:
        attr_test = generate_attr_test(attr)
        print attr, 'gain', gain(sample_dataset, attr_test, 1)