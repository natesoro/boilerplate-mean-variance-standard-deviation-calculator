import numpy as np

def calculate(list):

    if (len(list)<9):
        raise ValueError('List must contain nine numbers.')
    
    a2=np.array(list).reshape(3,3)

    mean1=np.mean(a2, axis=0).tolist()
    mean2=np.mean(a2, axis=1).tolist()
    mean3=np.mean([np.mean(mean1),np.mean(mean2)])

    var1=np.var(a2, axis=0).tolist()
    var2=np.var(a2, axis=1).tolist()
    var3=np.var(a2)

    dev1=np.std(a2, axis=0).tolist()
    dev2=np.std(a2, axis=1).tolist()
    dev3=np.std(a2)

    max1=np.max(a2, axis=0).tolist()
    max2=np.max(a2, axis=1).tolist()

    min1=np.min(a2, axis=0).tolist()
    min2=np.min(a2, axis=1).tolist()
    
    #alternative method
    sum1=[np.sum(a2[:,0]), np.sum(a2[:,1]), np.sum(a2[:,2])]
    sum2=[np.sum(a2[0]), np.sum(a2[1]), np.sum(a2[2])]
    
    calculations={
        "mean": [mean1, mean2, mean3],
        "variance": [var1, var2, var3],
        "standard deviation": [dev1, dev2, dev3],
        "max": [max1, max2, np.max(a2)],
        "min": [min1, min2, np.min(a2)],
        "sum": [sum1, sum2, np.sum(a2)]
    }
    return calculations