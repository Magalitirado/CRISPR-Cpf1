def reverse_complement(dna_sequence):
    complement = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    reverse_comp = ''.join([complement[base] for base in reversed(dna_sequence)])
    return reverse_comp

def reverse_sequence(dna_sequence):
    reverse = dna_sequence[::-1]
    return reverse

def complement_sequence(dna_sequence):
    complement = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    comp = ''.join([complement[base] for base in dna_sequence])
    return comp
