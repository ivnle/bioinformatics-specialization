def HammingDistance(p: str, q: str) -> int:
    hd: int = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd
