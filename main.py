

from data_preprocessing.demo import adder

from zinc_id.get_zincid import get_zincid_from_smile

zinc_id = get_zincid_from_smile("ClC1=CC(NC(=O)CSC2=NC=CC(=N2)C2=CSC(=N2)C2=CC=CC=C2)=CC(Cl)=C1")
print(zinc_id)