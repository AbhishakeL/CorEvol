# -*- coding: utf-8 -*-
"""
Created on Fri Feb  11 15:03:19 2018

@author: abhishake
"""




from Bio import SeqIO
import sys
import glob ,os
#record = SeqIO.read("GCA_000008865.1_ASM886v1_genomic.gbff", "genbank")


folder = sys.argv[1]
os.chdir(folder)
for file in glob.glob("*.gbk"):

    record = SeqIO.read(file, "genbank")

    outname = file +".cds"
    out_pro = outname +".pro"
    ref_cds = file +".refcds"

#output_handle = open("584_cds.fasta", "w")

    output_handle = open(outname,"w")
    protein_handle = open(out_pro,"w")
    refcds_handle = open(ref_cds,"w")
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
    """Here we are considering only those cds sequences which have a translated sequences in the file itself
    """

    for feature in record.features:
        if feature.type == "CDS" and "translation" in feature.qualifiers:
            count = count + 1
            
 

	
            feature_seq = feature.extract(record.seq)
            st = (feature.location.start +1)
            start_loc = str(st)
            en = (feature.location.end)
            end_loc = str(en)
            feature_name = file + "_" + start_loc + "_" + end_loc + "_" + str(count)
            pro_feat_name = file + "_" + start_loc + "_" + end_loc + "_" + str(count)
       
            output_handle.write(">" + str(feature_name) + "\n" + str(feature_seq) + "\n")
            protein_handle.write(">" + str(pro_feat_name) + "\t" + str(feature.qualifiers["translation"].pop()) + "\n")
            refcds_handle.write(">" + str(feature_name) + "\t" + str(feature_seq) + "\n")
            
    output_handle.close()
    protein_handle.close()
    refcds_handle.close()
#    print(str(count) + " CDS sequences extracted from " + str(file) )
