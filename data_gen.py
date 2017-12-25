import numpy as np
def read_phn (file_location):
    """reads phn file and returns list of phoneme delimiters
       and a list of the corresponding phonemes """
    phn_tab = [line.split() for line in open(file_location) ]
    delimiters = []
    labels = []
    for i in range ( len (phn_tab ) ):
        delimiters.append ( [phn_tab[i][0],phn_tab[i][1]])
        labels.append(phn_tab[i][2])
    return delimiters,labels
