from Bio import SeqIO

for record in SeqIO.parse("homosapien.fasta", "fasta"):
    print("ID:", record.id)
    print("Length:", len(record.seq))
