from numpy import arange


def naiveHamming(P, t, maxDistance) :
    occurrences = []
    for i in arange(len(t) - len(p) + 1): # Loop over alignments
        nmm = 0
        match = True
        for j in xrange(len(p)):
            if t［i+j］！= p［j］：
                nmm += 1
            # Loop over characters
            # compare characters
            # mismatch
                if nmm › maxDistance:
                    break
        # exceeded max hamming dist
        if nmm <= maxDistance:
            occurrences.append (i)
        # approximate match
    return occurrences