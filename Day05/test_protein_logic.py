
import unittest

from protein_logic import (
    calculate_molecular_weight,
    calculate_amino_acid_composition,
    parse_fasta_lines,
    analyze_protein
)


class TestProteinLogic(unittest.TestCase):

    def test_molecular_weight(self):
        result = calculate_molecular_weight("A")
        self.assertAlmostEqual(result, 89.0941, places=3)

    def test_amino_acid_composition(self):
        result = calculate_amino_acid_composition("AACC")
        self.assertEqual(result["A"], 50.0)
        self.assertEqual(result["C"], 50.0)

    def test_parse_fasta_lines(self):
        fasta = [
            ">Protein_1",
            "ACDE",
            ">Protein_2",
            "FGHI"
        ]
        result = parse_fasta_lines(fasta)
        self.assertEqual(result["Protein_1"], "ACDE")
        self.assertEqual(result["Protein_2"], "FGHI")

    def test_analyze_protein(self):
        result = analyze_protein("Test", "AC")
        self.assertEqual(result["name"], "Test")
        self.assertEqual(result["length"], 2)
        self.assertAlmostEqual(result["weight"], 192.23, places=2)

    def test_empty_sequence(self):
        with self.assertRaises(ValueError):
            calculate_molecular_weight("")

    def test_invalid_amino_acid(self):
        with self.assertRaises(ValueError):
            calculate_molecular_weight("AX")

    def test_empty_fasta(self):
        with self.assertRaises(ValueError):
            parse_fasta_lines([])

    def test_fasta_without_header(self):
        with self.assertRaises(ValueError):
            parse_fasta_lines(["ACDEFG"])

    def test_invalid_amino_acid_composition(self):
        with self.assertRaises(ValueError):
            calculate_amino_acid_composition("ACX")


if __name__ == "__main__":
    unittest.main()
