from progress.bar import IncrementalBar
    
def mis_in_genome(mis,genome,pos_init, progress = True):
    print(str(pos_init))
    if progress == True:
        bar = IncrementalBar('Loading...', max = len(mis))
    all_pos = []
    all_pos.append(pos_init)
    for i,seq in enumerate(mis):
        if progress == True:
            bar.next()
        for j in range(-len(seq),-15):
            sub_seq = str(seq[:-j])
            pos = genome.find(sub_seq)
            if pos != pos_init and pos not in all_pos and pos > 0:
                print(sub_seq+'\t'+str(pos))
                all_pos.append(pos)
    if progress == True:
        bar.finish()
    return all_pos

def mis_rev_in_genome(mis,genome,pos_init, progress = True):
    if progress == True:
        bar = IncrementalBar('Loading...', max = len(mis))
    all_pos = []
    for i,seq in enumerate(mis):
        if progress == True:
            bar.next()
        for j in range(0,12):
            pos=genome.find(str(seq[j:28]))
            if pos != pos_init and pos not in all_pos and pos >=0:
                all_pos.append(pos)
    if progress == True:
        bar.finish()
    return all_pos
