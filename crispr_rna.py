def search_crrna(genome,pam):
       
    grnas = []
        
        # Open file to write results in
    results = open('crispr_rna.txt','w')
    
        # Find all occurrences of the motif in the genomic sequence
    mini = int(input('\nWhere to begin: '))
    maxi = int(input('Where to stop: '))
    results.write('\nLooking from '+str(mini)+' to '+str(maxi)+'\n\n')
    for motif in pam:
        motif_positions = []
        pos = genome.find(motif)
        while pos >= 0:
            motif_positions.append(pos)
            pos = genome.find(motif, pos+1)
   
        # Print out the results
        if len(motif_positions) > 0:
            for pos in motif_positions:
                if pos > mini and pos < maxi:
                    results.write(str(pos)+'\t'+genome[pos:pos+28]+'\n')
                    grnas.append(genome[pos:pos+28])
    return grnas   
