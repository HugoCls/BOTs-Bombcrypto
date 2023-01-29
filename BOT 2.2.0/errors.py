import read

errors=read.lire('errors.txt')

def RESET():
    file=open('errors.txt','w')
    file.write('0')
    file.close()
    
def COUNT():
    file=open('errors.txt','r')
    txt=file.read()
    file.close()
    return(txt)

def ADD(i):
    file=open('errors.txt','r')
    txt=file.read()
    file.close()
    file=open('errors.txt','w')
    file.write(str(int(txt)+i))
    file.close()