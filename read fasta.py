from Bio import SeqIO

for record in SeqIO.parse("homosapien.fasta", "fasta"):
    print(record.id)
    print(record.seq)
