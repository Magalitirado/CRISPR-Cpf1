# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:16:06 2023

@author: Pro
"""

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

