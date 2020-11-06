primer1 = "AACCTTAAGGCCTTGGAA"
primer2 = "CCTTGGTTGGAAAATTGG"
dna_to_bin = {"A": "00", "C": "01", "T": "11", "G": "10"}

dna_B1 = ''.join(dna_to_bin[i] for i in primer1)
dna_B2 = ''.join(dna_to_bin[i] for i in primer2)

print(dna_B1)
print(dna_B2)

a = "".join(str(int(i == j)) for i, j in zip(dna_B1, dna_B2))

print(a.count("1"))