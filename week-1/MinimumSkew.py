def MinimumSkew(genome: str) -> list:
    results: list = [0]
    j: int
    for j in range(len(genome)):
        if genome[j] == 'G':
            results.append(results[j] + 1)
        elif genome[j] == 'C':
            results.append(results[j] - 1)
        else:
            results.append(results[j])
    min_skew: int = min(results)
    answer: list = []
    for index, skew in enumerate(results):
        if skew == min_skew:
            answer.append(index)
    return answer
            