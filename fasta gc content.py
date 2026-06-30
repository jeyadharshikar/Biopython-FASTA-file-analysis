from Bio import SeqIO

for record in SeqIO.parse("homosapien.fasta", "fasta"):

    dna = record.seq

    gc = (((dna.count("G") + dna.count("C")) / len(dna)) * 100)

    print(record.id)
    print("GC Content =", gc,"%")
