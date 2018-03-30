def to_rna(dna_strand: str) -> str:
    dna_rna_complements = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna_strand = ""
    for char in dna_strand.upper():
        if char not in dna_rna_complements.keys():
            raise ValueError("Invalid DNA nucleotide provided")
        else:
            rna_strand += dna_rna_complements[char]
    return rna_strand