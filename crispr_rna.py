# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:30:50 2023

@author: Pro
"""

def search_cpf1_rna(file):
    # Open the genomic text file
    with open(file, 'r',) as gen_file:
        
        # Open file to write results in
        results = open('crispr_rna.txt','w')
        
        # Read in the entire file as a string
        genomic_sequence = gen_file.read()
    
        # Get motifs
        motifs = ['tta','ttc','ttg']
    
        # Find all occurrences of the motif in the genomic sequence
        mini = int(input('Where to begin:'))
        maxi = int(input('Where to stop:'))
        for motif in motifs:
            results.write(motif.upper()+'\n\n')
            motif_positions = []
            pos = genomic_sequence.find(motif)
            while pos >= 0:
                motif_positions.append(pos)
                pos = genomic_sequence.find(motif, pos+1)
   
            # Print out the results
            if len(motif_positions) > 0:
                for pos in motif_positions:
                    if pos > mini and pos < maxi:
                        results.write(str(pos)+'\t'+genomic_sequence[pos:pos+28]+'\n')

search_cpf1_rna('streptomyces_ambofaciens_03.txt')         

   
