import re
import sys
from progress.bar import IncrementalBar

import crispr_rna
import generate_sequences
import mismatch
import reverse_complement
import line_break
import check_seq

# Select genome

genome = input('\nWhat is the genome file name?\n')

try:
    genome = open(genome,'r')
except FileNotFoundError:
    print('This file does not exist or is placed in another directory\n')

genome = genome.read()

line_break.line_break(genome)
genome = open('good_genome.txt','r')
genome = genome.read()

# Get gRNAs

grna = input('Do you want to look for a given gRNAs? Please enter sequence:\n')

if grna == '':
    
# Select CRISPR strategy

    crispr = input('\nWhich CRISPR strategy are you using? (Cas9 or Cpf1)\n')
    
    if crispr == 'Cas9':
        pam_sequence =['agg','tgg','cgg','ggg']
    elif crispr == 'Cpf1':
        pam_sequence = ['tta','ttc','ttg']
    else:
        print('This CRISPR system is not known from this program\n')
        sys.exit()

# Searching gRNA

    grnas = crispr_rna.search_crrna(genome, pam_sequence)
    
else:
    check_seq.check_seq(grna)
    grnas = []
    grnas.append(grna)
    
#grnas = ['ttggggcctctggcagcaggccagcacc']

# Searching for mismatches

## Open file for results

results = open('results.txt','a')

## Get results

i = 1
for seq in grnas:
    print('Analyzing RNA '+str(i)+' out of '+str(len(grnas))+' - '+str(seq))
    
    seq_rev_comp = seq[:-3]
    seq_rev_comp = reverse_complement.reverse_complement(seq_rev_comp)
    pos_init = genome.find(seq)
    
    results.write('Guide RNA:\t'+str(seq)+'\t'+str(pos_init)+'\n')
    
    all_mis = []
 
### Looking for mismatches at 0bp    
 
    nb_mis0 = 0
    i = len(seq)
    for j in range(-i,-15):
        pos = genome.find(seq[:-j])
        if pos >= 0 and pos != pos_init:
            nb_mis0 +=1
        pos = genome.find(seq_rev_comp[:-j])
        if pos >= 0 and pos != pos_init:
            nb_mis0 +=1
                
    results.write('Mis 0bp\t'+str(nb_mis0)+'\n')
            
    if nb_mis0 == 0:
        
### Looking for mismatches at 1bp

        save = [seq]
        seq = re.findall('\D',seq)
        
        mis1 = []
        mis1 = generate_sequences.generate_mismatch(seq,save,mis1)
        found_mis = mismatch.mis_in_genome(mis1, genome, pos_init, False)
        nb_mis1 = len(found_mis)
        for element in mis1:
            all_mis.append(element)

#### Looking for mismatches at 1bp with reverse complement

        if nb_mis1 == 0:
            print('Now reverse complement: '+str(seq_rev_comp))
            seq_rev_comp = re.findall('\D',seq_rev_comp)
            mis1_rev_comp = []
            for mis in mis1:
                mis1_rev_comp.append(reverse_complement.reverse_complement(mis))
            print('Mis1 rev comp: '+str(mis1_rev_comp[:3])+'...')
            found_mis = mismatch.mis_rev_in_genome(mis1_rev_comp, genome, pos_init)
            nb_mis1 += len(found_mis)
        else:
            print('Mismatches found: ' + str(found_mis))
            results.write('Stop at Mis1: ' + str(nb_mis1)+'\n')
        results.write('Mis 1bp\t'+str(nb_mis1)+'\n')

### Looking for mismatches at 2bp

        if nb_mis1 != 0:
            print('Program stoped because Mis1bp = ' + str(nb_mis1) +'\n')
            
        else:
            print('Now looking for 2bp mismatches')
            bar = IncrementalBar('Loading...', max = len(mis1))
            nb_mis2 = 0
            for mis in mis1:
                bar.next()
                mis = re.findall('\D',mis)
                mis2 = []
                mis2 = generate_sequences.generate_mismatch(mis, all_mis, mis2)
                found_mis = mismatch.mis_in_genome(mis2, genome, pos_init, False)
                nb_mis2 += len(found_mis)
                for element in mis2:
                    mis2_rev_comp = []
                    for mis in mis2:
                        mis2_rev_comp.append(reverse_complement.reverse_complement(mis))
                found_mis = mismatch.mis_rev_in_genome(mis2_rev_comp, genome, pos_init, False)
                nb_mis2 += len(found_mis)
            bar.finish()
            results.write('Mis 2bp\t'+str(nb_mis2)+'\n')
            
    i += 1
