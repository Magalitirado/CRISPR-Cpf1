import crispr_rna.py
import generate_sequences.py
import mismatch.py

# Look for gRNA in genome

search_cpf1_grna('streptomyces_ambofaciens_03.txt')


# Find mismatches sequences

grna = input('Enter the sequence of the chosen gRNA: ')
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
    
#Look for mismatches in genome

