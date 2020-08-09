from tabula import read_pdf, convert_into

def pdf_to_csv():
	convert_into("./data/smiles_pdf.pdf", "smiles.csv", output_format="csv", pages='all')
