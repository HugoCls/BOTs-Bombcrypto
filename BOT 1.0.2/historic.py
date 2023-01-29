import datetime
import read
import os

historic_path=read.lire(os.getcwd()+'\paths\historic_path.txt')[0]

def printt(text):
    fichier=open(historic_path,'a')
    now = datetime.datetime.now()
    mins=str(now.minute)
    if len(mins)==1:
        mins='0'+mins
    hour=str(now.hour)+':'+mins
    fichier.write(hour+' | '+text)
    print(hour+' | '+text)
    fichier.close()
    
def error():
    fichier=open(historic_path,'r')
    txt=fichier.read()
    fichier.close()
    if len(txt)==0:
        return(False)
    else:
        L = list(txt)
        N=L.count('$')
        if N>=10:
            l=len(L)-1
            piv=len(L)-1
            m=0
            while m<=10:
                if L[piv]=='$':
                    m+=1
                piv-=1
            L_cut=L[piv+1:l]
            txt_cut=''.join(str(e) for e in L_cut)
            l_cut=len(txt_cut)-1
            if l_cut>=55:
                if '<@150673899963678720>' in txt_cut[l_cut-50:l_cut]:
                    txt_cut='$'
            return((txt_cut.count('Connect'))>=4)
                
        else:
            return(False)