from Bio import SeqIO

for record in SeqIO.parse("homosapien.fasta", "fasta"):

    print("ID:", record.id)
    trimmed= record.seq[:len(record.seq)//3*3]
    print("Protein:", trimmed.translate())
