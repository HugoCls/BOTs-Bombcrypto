import codecs

def lire(file_path):
    List=[]
    with codecs.open(file_path, encoding='utf-8') as f:
        for line in f:
            List.append(line.strip())
    return(List)