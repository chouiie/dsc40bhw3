def histogram(points, bins):

    n = len(points)
    k = len(bins)
    counts = [0] * k

    bin_index = 0
    for point in points:
        while bin_index < k - 1 and point >= bins[bin_index][1]:
            bin_index += 1
        counts[bin_index] += 1

    densities = []
    for i in range(k):
        a, b = bins[i]
        width = b - a
        density = counts[i] / (n * width)
        densities.append(density)

    return densities