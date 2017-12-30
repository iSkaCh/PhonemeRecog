
import numpy as np 
import glob
from scipy.io.wavfile import read
from scipy.io.wavfile import write
phoneme_list = ['b','d','g','p','t','k','dx','q','jh','ch','s','sh','z','zh','f','th','v',
                'dh','m','n','ng','em','en','eng','nx','l','r','w','y','hh','hv','el',
                'iy','ih','eh','ey','ae','aa','aw','ay','ah','ao','oy','ow','uh',
                'uw','uh','uw','ux','er','ax','ix','axr','ax-h','pau','epi','h#',
                '1','2','bcl','dcl','gcl','pcl','tcl','kcl']
def read_phn (file_location):
    
    """reads phn file and returns list of phoneme delimiters
       and a list of the corresponding phonemes """
    phn_tab = [line.split() for line in open(file_location) ]
    
    statsfile  = open ("stats.txt",'r+')
    stats = [line.split() for line in statsfile ]
    if len (stats) >0:
        maxlen = int (stats[0][1] )
        minlen =int ( stats[1][1])
    else :
        maxlen = 0
        minlen =100000        
    
    
    delimiters = []
    labels = []
    
    
    for i in range ( len (phn_tab ) ):
        begin, end = int(phn_tab[i][0]) ,int(phn_tab[i][1])
        if end - begin > maxlen : maxlen = end-begin 
        if end -begin< minlen : minlen = end-begin
        delimiters.append ( [begin, end])
        labels.append(phn_tab[i][2])
    statsfile.truncate(0)
    statsfile.write ( "maxlen  "+str(maxlen)+"\n")
    statsfile.write ( "minlen  "+str(minlen)+"\n")
    statsfile.close()
    
    return delimiters,labels
def wav_2_ph(folder):
    """generates list of phoneme data and labels"""
    wavfile_list =glob.glob(folder+"/**/*RIFF.wav",recursive=True)
    ph_data = []
    labels_list = []
    for wavfile in wavfile_list[:10] :
        phnfile= wavfile [0:len(wavfile)-8]+".PHN"
        data_table = read (wavfile)[1]
        delimiters, labels = read_phn (phnfile)
        labels_list.append (labels)
        i=0
        print ( phnfile )
        for delimiter in delimiters :
            #if delimiter[1]-delimiter[0] == 32 :
                #print (wavfile)
                #break
            #if delimiter[1]-delimiter[0] == 74285 : 
                #print (wavfile)
                #break
            y = np.zeros(65)
            y[phoneme_list.index(labels[i])] = 1
            ph_data.append( [data_table[delimiter[0]:delimiter[1]],y])
            i+=1
    return ph_data

if __name__ == '__main__':
    ph_data = wav_2_ph("files\TIMIT\TRAIN")
    print (ph_data)
