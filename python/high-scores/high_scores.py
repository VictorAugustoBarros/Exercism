def latest(scores):
    return scores[-1]


def personal_best(scores):
    return sorted(scores)[-1]


def personal_top_three(scores):
    arr_new = []
    tmp_scores = sorted(scores)
    len_scores = 3 if len(scores) > 3 else len(scores)

    for i in range(0, len_scores):
        arr_new.append(tmp_scores[-1])
        del tmp_scores[-1]

    return arr_new
