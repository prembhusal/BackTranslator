
import random

codonTable = {
    'A': ('GCT', 'GCC', 'GCA', 'GCG'),
    'C': ('TGT', 'TGC'),
    'D': ('GAT', 'GAC'),
    'E': ('GAA', 'GAG'),
    'F': ('TTT', 'TTC'),
    'G': ('GGT', 'GGC', 'GGA', 'GGG'),
    'I': ('ATT', 'ATC', 'ATA'),
    'H': ('CAT', 'CAC'),
    'K': ('AAA', 'AAG'),
    'L': ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'),
    'M': ('ATG',),
    'N': ('AAT', 'AAC'),
    'P': ('CCT', 'CCC', 'CCA', 'CCG'),
    'Q': ('CAA', 'CAG'),
    'R': ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'),
    'S': ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'),
    'T': ('ACT', 'ACC', 'ACA', 'ACG'),
    'V': ('GTT', 'GTC', 'GTA', 'GTG'),
    'W': ('TGG',),
    'Y': ('TAT', 'TAC'),
    '*': ('TAA', 'TAG', 'TGA'),
}

def backTranslateSeq(aaSeq):
	#convert amino acid sequence to nucleotide sequence 
	ntSeq=''
	for char in aaSeq:
		listCodon = list(codonTable[char])
		random.shuffle(listCodon)
		#print listCodon
		ntSeq +=listCodon[0]

	return ntSeq


def calculateGC(ntSeq):
	seqList = list(ntSeq.upper())
	g = seqList.count("G")
	c = seqList.count("C")

	return (g+c)/float(len(seqList))

def ntSeqInGCrange(aaSeq, gcRange):
	#aaSeq = amino acid sequence
	#gcRange = gc range (eg. 40-60)
	
	ntSeq =''
	tempGC =0.0
	ranges = gcRange.split("-")
	#find the new nucleotide sequence until the specified gc range is reached
	while not (tempGC *100 >= float(ranges[0]) and tempGC*100 <= float(ranges[1])):
		ntSeq = backTranslateSeq(aaSeq)
		tempGC = calculateGC(ntSeq)
	return ntSeq,tempGC
#print backTranslateSeq("TTYNYMRQLVVDVVITNHYSV")
#print ntSeqInGCrange("TYNYMRQLVVDVVITNHYSV", "40-60")

