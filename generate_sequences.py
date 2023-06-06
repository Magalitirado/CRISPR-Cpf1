def generate_mismatch(seq,mis,results):
# grna : ARN guide
# seq : ARN guide pour mismatch 1 et mismatch 1 pour mismatch2, ...
# output : fichier d'écriture des résultats
# mis : liste des mismatchs déjà obtenu pour éviter les doublons
# space : caractère à intégrer après le résultat dans le fichier output

    for i, n in enumerate(seq):
        if i > 2:
            if n == 'a':
                seq[i] = 't'
                new = ''.join(seq)
                if new not in mis:
                    results.append(new)
                seq[i] = 'c'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.append(new)
                seq[i] = 'g'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.append(new)
                seq[i] = 'a'
            if n == 't':
                seq[i] = 'a'
                new = ''.join(seq)
                if new not in mis:
                    results.append(new)
                seq[i] = 'c'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.append(new)
                seq[i] = 'g'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.append(new)
                seq[i] = 't'
            if n == 'c':
                seq[i] = 't'
                new = ''.join(seq)
                if new not in mis:
                    results.append(new)
                seq[i] = 'a'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.append(new)
                seq[i] = 'g'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.append(new)
                seq[i] = 'c'
            if n == 'g':
                seq[i] = 't'
                new = ''.join(seq)
                if new not in mis:
                    results.append(new)
                seq[i] = 'c'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.append(new)
                seq[i] = 'a'
                new = ''.join(seq)
                if ''.join(seq) not in mis:
                    results.append(new)
                seq[i] = 'g'
    return results
