def swap_sum(A, B):

    sum_a = sum(A)
    sum_b = sum(B)


    diff = sum_b - sum_a - 10
    if diff % 2 != 0:
        return None

    target = diff // 2


    i = 0
    j = 0

    while i < len(A) and j < len(B):
        current_diff = B[j] - A[i]
        if current_diff == target:
            return (i, j)
        elif current_diff < target:

            j += 1
        else:
            i += 1

    return None