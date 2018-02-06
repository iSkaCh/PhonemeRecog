
import numpy as np 
import glob
from scipy.io.wavfile import read
from scipy.io.wavfile import write
phoneme_list = ['b','d','g','p','t','k','dx','q','jh','ch','s','sh','z','zh','f','th','v',
                'dh','m','n','ng','em','en','eng','nx','l','r','w','y','hh','hv','el',
                'iy','ih','eh','ey','ae','aa','aw','ay','ah','ao','oy','ow','uh',
                'uw','uh','uw','ux','er','ax','ix','axr','ax-h','pau','epi','h#',
                '1','2','bcl','dcl','gcl','pcl','tcl','kcl']# liste de tout les phoneme permet de generer le one hot encoding


def read_phn (file_location):
    
    """reads phn file and returns list of phoneme delimiters
       and a list of the corresponding phonemes """ 
    phn_tab = [line.split() for line in open(file_location) ] # on lit le fichier ligne par ligne et on cree une liste contenant les differente ligne 
    delimiters = []
    labels = []
    for i in range ( len (phn_tab ) ):
        # on creer une nouvelle liste contenant les date debut et fin de chaque phoneme et son label
        begin, end = int(phn_tab[i][0]) ,int(phn_tab[i][1]) 
        delimiters.append ( [begin, end])
        labels.append(phn_tab[i][2])

    
    return delimiters,labels
def wav_2_ph(folder):
    """generates list of phoneme data and labels"""
    wavfile_list =glob.glob(folder+"/**/*RIFF.wav",recursive=True)# genere une liste contenant les fichiers WAV dans folder
    ph_data = [] # liste globale contenant les donnees brut et le label correspondant 
    for wavfile in wavfile_list :
        # pour chaque fichier wav on extrait les donnees brut, on le devise selon les delimiteur extrait du fichier phn et on ajout les deux à la liste global
        phnfile= wavfile [0:len(wavfile)-8]+".PHN" #genere l'emplacement du fichier phn correspondant au fichier wav
        data_table = read (wavfile)[1] # extraction des donnees brut
        delimiters, labels = read_phn (phnfile) # extraction des delimiteur de phonemes et labels correspondants
        i=0
        print ( phnfile )
        for delimiter in delimiters :
            y = np.zeros(65)
            y[phoneme_list.index(labels[i])] = 1 # creation du one hot encoding du phoneme
            ph_data.append( [data_table[delimiter[0]:delimiter[1]],y])
            i+=1
    print( "total phonemes: ", len(ph_data))
    return ph_data

if __name__ == '__main__':
    ph_data = wav_2_ph("files\TIMIT\TRAIN")
    print (ph_data[:,0])