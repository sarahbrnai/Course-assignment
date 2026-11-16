from protein_logic import (
    read_fasta,
    analyze_protein
)


def main():

    proteins = read_fasta("rcsb_pdb_1A7F.fasta")

    for name, sequence in proteins.items():

        result = analyze_protein(name, sequence)

        print("Protein:", result["name"])
        print("Sequence length:", result["length"])
        print("Molecular weight:", result["weight"], "Da")

        print("Amino acid composition:")

        for aa, percentage in result["composition"].items():
            print(aa, ":", percentage, "%")

        print("----------------------")


if __name__ == "__main__":
    main()