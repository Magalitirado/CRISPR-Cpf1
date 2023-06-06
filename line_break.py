import sys

def line_break(genome):
    genome = open(genome,'r')
    genome = genome.read()
    results = input('What is the name of the new file?\n')
    results = open('good_genome.txt','w')
    for i in genome:
        if i != '\n':
            results.write(i.lower())
        elif i not in ['a','t','c','g']:
            print('This genome is not only containing nucleotides...\n')
            sys.exit()
    results.close()
