####This script should take a fasta and return the longest isoform. This is based on the augustus.hints.aa file after BRAKER2 annotation
##Written by Hunter K. Walt 28 July 2022
#Call from command line: python3 get_longest_isoform.py [output file name]

from Bio import SeqIO
import sys

records = list(SeqIO.parse("augustus.hints.aa", "fasta"))

iso_list = []
iso_ids = []

longest_iso = []
iso_dict = {}

for record in records:					#iterate through seqio objects
	if record.id[:-3] not in iso_dict.keys():	#take the gene names 
		iso_dict[record.id[:-3]] = []		#initialize a dictionary of lists: the keys are the gene names, and the list values are the isoforms.



for record in records:					#iterate through records again
	rec = record.id[:-3]				#take gene name again
	if rec in iso_dict:				#populate value lists with full records
		iso_dict[rec].append(record)


for k,v in iso_dict.items():				#iterate through dictionary
	l = 0						#initialize length variable
	for i in v:
		if len(i.seq) > l:			#get longest isoform
			l = len(i.seq)			#save length of longest sequence
			longest = i			#save record of longest sequence	
		else:
			continue

	longest_iso.append(longest)			#make list of longest seqio records

print("You started with "+str(len(records))+" sequences.")					#compare number of sequences
print("You ended with "+str(len(longest_iso))+" sequences.")

SeqIO.write(longest_iso, sys.argv[1] , "fasta") 	#write out file
					
	
	
