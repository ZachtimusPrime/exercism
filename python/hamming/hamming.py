def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) == len(strand_b):
        hamming_distance = 0
        for index in range(0,len(strand_a)):
            if strand_a[index] != strand_b[index]:
                hamming_distance += 1
        return hamming_distance
    else:
        raise ValueError("DNA strand lengths are not the same")
