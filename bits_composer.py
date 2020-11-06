name_in = "/Users/marek//primers/experyment.txt"


def complement(string):
    trans = {"A": "T", "C": "G", "T": "A", "G": "C"}
    answer = ''.join(trans[i] for i in string)
    return answer


file_in = open(name_in, "r")
primers = file_in.readlines()

bit_sequence = "0101001101111010"
number_of_bits = len(bit_sequence)
number_of_primers = len(primers)

if number_of_bits > number_of_primers:
    exit(1)

print("Number of bits: ", number_of_bits)
print("Bit sequence: ", bit_sequence, '\n')

bit_0 = primers[0][:-1]
bit_1 = primers[1][:-1]
bits = [bit_0, bit_1]
sep = ""

print("Bit 0: ", bit_0, ' --R-complement-->', complement(bit_0))
print("Bit 1: ", bit_1, ' --R-complement-->', complement(bit_1))

for i in range(2, number_of_bits + 2):
    print('S_{0:<2} :  {1}'.format(i - 2, primers[i][:-1]))

print("\nSTARTER\n")
print('   {0:19} {1:19} {2:19}'.format('S_0', 'BIT', 'S_1'), sep='')
starter = primers[2][:-1] + sep + bits[int(bit_sequence[0])] + sep + primers[3][:-1]
print('  ', starter, '\n')

for i in range(4, number_of_bits + 3):
    strand = primers[i - 1][:-1] + bits[int(bit_sequence[i - 3])] + primers[i][:-1]
    print('   S_{0:<18}Bit_{1:16}S_{2:<22}'.format(i - 2, bit_sequence[i - 3], i - 3), end='')
    print('   S_{0:<18}Bit_{1:16}S_{2:<19}'.format(i - 3, bit_sequence[i - 3], i - 2))
    print('5\' ', end='')
    print(complement(strand[::-1]), ' <-- ', complement(strand))
