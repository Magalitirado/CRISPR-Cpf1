# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 17:40:28 2023

@author: Pro
"""
import re

def search_motif(grna,motifs,genome):
    all_pos = []
    genome = open(genome,'r')
    genome = genome.read
    genome = re.findall(r'\D',genome)
    print(str(motifs))
    motifs = open(motifs,'r')
    motifs = motifs.readlines()
    results = open('mismatch_results.txt','w')
    for element in motifs:
        for j in range(-28,-15):
            if element[:-j+1] != grna[:-j]:
                element = re.findall(r'\D',element)
                pos = genome.find(str(element[:-j+1]))
                if pos >= 0 and pos not in all_pos:
                    all_pos.append(pos)
                    results.write(str(element[:-j+1])+'\t'+str(pos))
    
    
                
search_motif('ttcgacgtcgcctccgcgacacacaccc','mismatch1.txt','streptomyces_ambofaciens_03.txt')
                

#        for j in range(-28,-15):
#            grna = grna[:-j]
#            motifs = generate_mismatch(grna, grna, mis)
#            print('Motifs : '+str(motifs[:2]))
#            for seq in motifs:
#                pos = genomic_sequence.find(str(seq)[:-j].lower())
#                if pos >= 0 and pos not in motif_positions:
#                    motif_positions.append(pos)
#        results.write(str(len(motif_positions))+'\n')



            
#pos = genomic_sequence.find(str(seq)[:-j].lower())
        
#grna = input('Quelle est la séquence de l\'ARN guide : ')

#sequences = ['cggagcgggtaccacatcgctgcgcgat','ggagcgcggggcctacggccccgatggg']


#results = open('mismatch_results.txt','a')
#mis1_pos = search_motif(grna,sequences,'streptomyces_ambofaciens.txt')
#print('Mismatch 1bp :\t'+str(len(mis1_pos)))

#mis2 = []
#for seq in mis1:
#    mis_inter = generate_mismatch(grna, seq)
#    for element in mis_inter:
#        if element not in mis1:
#            mis2.append(element)
#print('mismatch 2 : '+str(mis2[:2])+'... : '+str(len(mis2))+' sequences')

#mis3 = []
#for seq in mis2:
#    mis_inter = generate_mismatch(grna, seq)
#    for element in mis_inter:
#        if element not in mis1 and element not in mis2:
#            mis3.append(element)
#print('mismatch 3 : '+str(mis3[:2])+'... : '+str(len(mis3))+' sequences')
    
    # Open the genomic text file
#    gen_file = open('streptomyces_ambofaciens_03.txt', 'r')
        
    # Open file to write results in
#    results = open('results.txt','a')
    
    # Read in the entire file as a string
#    genomic_sequence = gen_file.read()
#    grna = input('Quelle est la séquence de l\'ARN guide : ')
#    grna = re.findall(r'\D',grna)
#    motif_positions = []
#    results.write('ARN guide : '+str(''.join(grna))+'\n')
#    mis = []
    # Get motifs
#        motif = input('Quelle est la séquence : ')
 
    # Find all occurrences of the motif in the genomic sequence
#    for i in range(0,1):
#        results.write('Mimastch '+str(i+1)+' bp:\t')
        
#        for j in range(-28,-15):
#            grna = grna[:-j]
#            motifs = generate_mismatch(grna, grna, mis)
#            print('Motifs : '+str(motifs[:2]))
#            for seq in motifs:
#                pos = genomic_sequence.find(str(seq)[:-j].lower())
#                if pos >= 0 and pos not in motif_positions:
#                    motif_positions.append(pos)
#        results.write(str(len(motif_positions))+'\n')
            
                 
#search_motif()
#search_motif('mismatch2.txt')