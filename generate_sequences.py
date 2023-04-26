# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:16:06 2023

@author: Pro
"""

import re
    
def generate_mismatch(grna,seq,output,mis,space):
# grna : ARN guide
# seq : ARN guide pour mismatch 1 et mismatch 1 pour mismatch2, ...
# output : fichier d'écriture des résultats
# mis : liste des mismatchs déjà obtenu pour éviter les doublons
# space : caractère à intégrer après le résultat dans le fichier output
    

    results = open(output,'a')
    for i, n in enumerate(seq):
        if i > 2:
            if n == 'a':
                seq[i] = 't'
                new = ''.join(seq)
                if new not in mis:
                    results.write(new+space)
                seq[i] = 'c'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.write(new+space)
                seq[i] = 'g'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.write(new+space)
                seq[i] = 'a'
            if n == 't':
                seq[i] = 'a'
                new = ''.join(seq)
                if new not in mis:
                    results.write(new+space)
                seq[i] = 'c'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.write(new+space)
                seq[i] = 'g'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.write(new+space)
                seq[i] = 't'
            if n == 'c':
                seq[i] = 't'
                new = ''.join(seq)
                if new not in mis:
                    results.write(new+space)
                seq[i] = 'a'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.write(new+space)
                seq[i] = 'g'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.write(new+space)
                seq[i] = 'c'
            if n == 'g':
                seq[i] = 't'
                new = ''.join(seq)
                if new not in mis:
                    results.write(new+space)
                seq[i] = 'c'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.write(new+space)
                seq[i] = 'a'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.write(new+space)
                seq[i] = 'g'

# Ask for gRNA
grna = input('Enter the sequence of gRNA: ')
save = [grna]
print(save)
grna = re.findall(r'\D',grna)

generate_mismatch(grna,grna,'mismatch1.txt',save,'\n')

mis2 = ''.join(grna)+'\n'
mis2 = [mis2]
print('mis2: '+str(mis2))
mis1 = open('mismatch1.txt','r')
mis1 = mis1.readlines()

for i, line in enumerate(mis1):
    mis2.append(line)

for line in mis1:
    line = re.findall(r'\D',line)
    generate_mismatch(grna,line, 'mismatch2.txt',mis2,'')

mis3 = mis2
print('mis3:'+str(mis3[:2]))
mis2 =open('mismatch2.txt','r')
mis2 = mis2.readlines()

for i, line in enumerate(mis2):
    mis3.append(line)
    
for line in mis2:
    line = re.findall(r'\D',line)
    generate_mismatch(grna,line,'mismatch3.txt',mis3,'')
