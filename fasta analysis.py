from Bio import SeqIO

for record in SeqIO.parse("homosapien.fasta", "fasta"):

    dna = record.seq
    print("Sequence ID:", record.id)
    print("Sequence:", dna)
    print("Length:", len(dna))
    gc = ((dna.count("G") + dna.count("C")) / len(dna)) * 100
    print("GC Content:", gc, "%")
    print("Reverse Complement:", dna.reverse_complement())
    trimmed = dna[:len(dna)//3*3]
    print("Protein:", trimmed.translate())
    print("RNA:", dna.transcribe())
