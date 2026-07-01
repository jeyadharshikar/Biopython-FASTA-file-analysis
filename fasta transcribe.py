from Bio import SeqIO

for record in SeqIO.parse("homosapien.fasta", "fasta"):

    print("ID:", record.id)
    print("Protein:", record.seq.transcribe())
