# Amino acid molecular weights (Da)

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


# Read protein sequences from a FASTA file
def parse_fasta_lines(lines):

    proteins = {}
    current_name = None

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith(">"):

            current_name = line[1:].strip()

            if not current_name:
                raise ValueError("Protein header cannot be empty.")

            proteins[current_name] = ""

        else:

            if current_name is None:
                raise ValueError("FASTA file must start with a header.")

            proteins[current_name] += line.upper()

    if not proteins:
        raise ValueError("No protein sequences found.")

    return proteins


def read_fasta(filename):

    with open(filename, "r", encoding="utf-8") as file:
        return parse_fasta_lines(file)


# Calculate protein molecular weight
def calculate_molecular_weight(sequence):

    sequence = sequence.upper()

    if not sequence:
        raise ValueError("Protein sequence is empty.")

    total_weight = WATER_MASS

    for amino_acid in sequence:

        if amino_acid not in amino_acids:
            raise ValueError("Invalid amino acid: " + amino_acid)

        total_weight += amino_acids[amino_acid]

    return total_weight


# Calculate amino acid composition
def calculate_amino_acid_composition(sequence):

    sequence = sequence.upper()

    if not sequence:
        raise ValueError("Protein sequence is empty.")

    composition = {}

    for amino_acid in sequence:

        if amino_acid not in amino_acids:
            raise ValueError("Invalid amino acid: " + amino_acid)

        composition[amino_acid] = composition.get(amino_acid, 0) + 1

    percentages = {}

    for amino_acid, count in composition.items():

        percentages[amino_acid] = round(
            count / len(sequence) * 100, 2
        )

    return percentages


# Analyze one protein
def analyze_protein(name, sequence):

    weight = calculate_molecular_weight(sequence)

    composition = calculate_amino_acid_composition(sequence)

    return {
        "name": name,
        "length": len(sequence),
        "weight": round(weight, 2),
        "composition": composition
    }