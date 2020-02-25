def Skew(genome: str) -> list:
    results: list = [0]
    j: int
    for j in range(len(genome)):
        if genome[j] == 'G':
            results.append(results[j] + 1)
        elif genome[j] == 'C':
            results.append(results[j] - 1)
        else:
            results.append(results[j])
    return results