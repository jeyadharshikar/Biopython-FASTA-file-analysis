from Bio import SeqIO

for record in SeqIO.parse("homosapien.fasta", "fasta"):

    dna = record.seq

    print("ID:", record.id)

    print("A =", dna.count("A"))
    print("T =", dna.count("T"))
    print("G =", dna.count("G"))
    print("C =", dna.count("C"))
