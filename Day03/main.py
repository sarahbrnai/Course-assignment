
# Molecular weight of each amino acid residue (Da)

from fileinput import filename


amino_acids = {
    "A": 71.0788,
    "R": 156.1875,
    "N": 114.1038,
    "D": 115.0886,
    "C": 103.1388,
    "E": 129.1155,
    "Q": 128.1307,
    "G": 57.0519,
    "H": 137.1411,
    "I": 113.1594,
    "L": 113.1594,
    "K": 128.1741,
    "M": 131.1926,
    "F": 147.1766,
    "P": 97.1167,
    "S": 87.0782,
    "T": 101.1051,
    "W": 186.2132,
    "Y": 163.1760,
    "V": 99.1326
}

WATER_MASS = 18.0153


def calculate_molecular_weight(sequence):

    sequence = sequence.upper()

    total_weight = WATER_MASS

    for amino_acid in sequence:

        if amino_acid not in amino_acids:
            raise ValueError("Invalid amino acid: " + amino_acid)

        total_weight += amino_acids[amino_acid]

    return total_weight

def read_fasta(filename):

    proteins = {}

    with open(filename, "r") as file:

        current_name = None

        for line in file:

            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):

                current_name = line[1:]
                proteins[current_name] = ""

            else:

                if current_name is None:
                    raise ValueError(
                        "FASTA file must start with a protein header (>)"
                    )

                proteins[current_name] += line

    return proteins

proteins = read_fasta("rcsb_pdb_1A7F.fasta")

for name, sequence in proteins.items():

    weight = calculate_molecular_weight(sequence)

    print("Protein:", name)
    print("Sequence length:", len(sequence))
    print("Molecular weight:", round(weight, 2), "Da")
    print("----------------------")