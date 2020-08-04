

from data_preprocessing.demo import adder

from zinc_id.get_zincid import get_zincid_from_smile

<<<<<<< HEAD
zinc_id = get_zincid_from_smile("FC(F)(F)C1=CC=C(NC(=O)CSC2=NC(=CC=N2)C2=CC(=NO2)C2=CC=C(Cl)C=C2Cl)C=C1")
print(zinc_id)


#from padelpy import from_smiles

# calculate molecular descriptors for propane
#descriptors = from_smiles('FC(F)(F)C1=CC=C(NC(=O)CSC2=NC(=CC=N2)C2=CC(=NO2)C2=CC=C(Cl)C=C2Cl)C=C1')


#print(type(descriptors))
#print(len(descriptors))
# in addition to descriptors, calculate PubChem fingerprints
#desc_fp = from_smiles('CCC', fingerprints=True)

# only calculate fingerprints
#fingerprints = from_smiles('CCC', fingerprints=True, descriptors=False)

# save descriptors to a CSV file
#_ = from_smiles('FC(F)(F)C1=CC=C(NC(=O)CSC2=NC(=CC=N2)C2=CC(=NO2)C2=CC=C(Cl)C=C2Cl)C=C1', output_csv='descriptors.csv')

from tabula import read_pdf, convert_into



convert_into("./data/smiles_pdf.pdf", "smiles.csv", output_format="csv", pages='all')
=======
zinc_id = get_zincid_from_smile("ClC1=CC(NC(=O)CSC2=NC=CC(=N2)C2=CSC(=N2)C2=CC=CC=C2)=CC(Cl)=C1")
print(zinc_id)

print("arun")
>>>>>>> 338f749d606b19c952ea08f4d7bf26fb8faa6970
