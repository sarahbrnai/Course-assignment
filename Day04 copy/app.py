from flask import Flask, render_template, request

from protein_logic import (
    parse_fasta_lines,
    analyze_protein
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    error = None

    if request.method == "POST":

        uploaded_file = request.files.get("fasta_file")

        if uploaded_file is None or uploaded_file.filename == "":
            error = "Please upload a FASTA file."

        else:

            try:

                content = uploaded_file.read().decode("utf-8")

                proteins = parse_fasta_lines(content.splitlines())

                for name, sequence in proteins.items():

                    result = analyze_protein(name, sequence)

                    results.append(result)

            except (ValueError, UnicodeDecodeError) as e:
                error = str(e)

    return render_template(
        "index.html",
        results=results,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True) 