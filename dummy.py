from Bio import SeqIO
record = SeqIO.read("GCA_000005845.2_ASM584v2_genomic.gbff", "genbank")
output_handle = open("584_cds.fasta", "w")
count = 0
#for feature in record.features:
#    if feature.type == "CDS":
 #       count = count + 1
        #feature_name = feature.qualifiers["protein_id"][0] # Use feature.qualifiers or feature.dbxrefs here
#	feature_name = "..."
	#print(feature_name)
#	feature_seq = feature.extract(record.seq)
        # Simple FASTA output without line wrapping:
 #       output_handle.write(">" + str(feature_name) + "\n" + str(feature_seq) + "\n")
#output_handle.close()

for feature in record.features:
    if feature.type == "CDS":
        count = count + 1
        feature_name = feature.qualifiers["locus_tag"][0] # Use feature.qualifiers or feature.dbxrefs here
        feature_seq = feature.extract(record.seq)
        # Simple FASTA output without line wrapping:
        output_handle.write(">" + str(feature_name) + "\n" + str(feature_seq) + "\n")
output_handle.close()
print(str(count) + " CDS sequences extracted")
