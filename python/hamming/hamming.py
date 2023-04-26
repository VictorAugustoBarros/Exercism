def distance(strand_a, strand_b):
    strand_a = list(strand_a)
    strand_b = list(strand_b)

    if len(strand_a) != len(strand_b):
        raise ValueError("Size do not match")

    hamming_dist = 0
    for i in range(0, len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming_dist += 1

    return hamming_dist
