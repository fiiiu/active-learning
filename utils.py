import numpy as np

def H(p):
    
    """
    Return the Shannon entropy of a distribution given as a discrete list of probabilities
    """
    #normalize & convert to numpy arrays
    pn=np.array([float(el)/np.linalg.norm(p) for el in p])
    
    h=0
    for pi in pn:
        if pi != 0:
            h-=np.log2(pi)*pi
            
    return h


def H(p, support, normalized=False):
    """
    Return the Shannon entropy of a distribution given as a function and its discrete support
    #MUST BE NORMALIZED --NO LONGER, just tell it! :)
    """
    entropy=0
    if normalized:
        for x in support:
            prob=p(x)
            if prob!=0:
                entropy-=np.log2(prob)*prob
        return entropy
    else:
        norm=0
        for x in support:
            prob=p(x)
            norm+=prob
            if prob!=0:
                entropy-=np.log2(prob)*prob
        return entropy/norm+np.log2(norm)





    