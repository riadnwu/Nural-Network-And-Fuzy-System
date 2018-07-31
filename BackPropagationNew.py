from math import exp
from random import uniform
import numpy as np

def forwardPass(wij,wjk,wkl):
    while(True):
        hiIn = additionBious(np.matmul(input, wij), m)# Hidden Layer 1
        hi = relu(hiIn)
        hjIn = additionBious(np.matmul(hi, wjk), o) # Hidden Layer 2
        hj = sigmoid(hjIn)
        hkIn =additionBious(np.matmul(hj,wkl),p) # Output Layer
        hk = softMax(hkIn)
        if float(format(hk[0],"0.2"))!= y[0] or  float(format(hk[1],"0.2"))!= y[1]:
            print (format(hk[0], "0.4"))+" : "+(format(hk[1],"0.4"))
            wij, wjk, wkl=backwardPass(wij,wjk,wkl,hiIn,hjIn,hkIn,hi,hj,hk)
            #print wjk
        else:
            print (format(hk[0], "0.2"))+(format(hk[1],"0.2"))
            break

def backwardPass(wij,wjk,wkl,hiIn,hjIn,hkIn,hi,hj,hk):
    nwkl,oOut,oIn = outputLayerToHiddenlayer2(wkl, hkIn, hk,hj)
    nwjk,h2In,eTotal=hiddenLayer2ToHiddenLayer1(wjk,wkl,hjIn,oOut,oIn,hi)
    nwij, e2Total=hiddenLayer1ToInput(wij, wjk, eTotal, h2In, hi)
    #print nwjk
    return nwij,nwjk,nwkl


def hiddenLayer1ToInput(wij,wjk,eTotal,h2In,hi):
    e2Total = []
    nwij = np.zeros((n, m), dtype='float')
    for i in range(m):
        e2Total.append(0)
        for j in range(o):
            e2Total[i] = e2Total[i] + (eTotal[i] * h2In[i] * wjk[i][j])
    for i in range(m):
        for j in range(o):
            nwij[i][j] = wij[i][j] - (learningRate * (e2Total[j] * hi[j] * input[i]))
    return nwij,e2Total

def hiddenLayer2ToHiddenLayer1(wjk,wkl,hjIn,oOut,oIn,hi):
    h2In=[]
    eTotal=[]
    nwjk = np.zeros((m, o), dtype='float')
    for i in range(o):
        h2In.append(sigmoid1(hjIn[i])*(1-sigmoid1(hjIn[i])))

    for i in range(o):
        eTotal.append(0)
        for j in range(p):
            eTotal[i]=eTotal[i]+(oOut[j] * oIn[j] * wkl[i][j])
    for i in range(m):
        for j in range(o):
            nwjk[i][j]=wjk[i][j]-(learningRate* (eTotal[j]*h2In[j]*hi[i]))
    return nwjk,h2In,eTotal


def outputLayerToHiddenlayer2(wkl,hkIn,hk,hj):
    oOut = []
    oIn = []
    nwkl = np.zeros((o, p), dtype='float')
    for i in range(p):
        oOut.append(-1 * ((y[i] * (1 / hk[i])) + ((1 - y[i]) * (1 / (1 - hk[i])))))
        oIn.append((exp(hkIn[0]) * exp(hkIn[1])) / ((exp(hkIn[0]) + exp(hkIn[1])) * (exp(hkIn[0]) + exp(hkIn[1]))))
    for i in range(o):
        for j in range(p):
            nwkl[i][j] =wkl[i][j]-(learningRate* (oOut[j] * oIn[j] * hj[j]))
    return nwkl,oOut,oIn





def relu(hi):
    for i in range(m):
        hi[i]=max(hi[i],0)
    return hi
def sigmoid(hj):
    for i in range(o):
        hj[i]=1/(1+exp(-hj[i]))
    return hj
def sigmoid1(w):
    w=1/(1+exp(-w))
    return w
def softMax(hk):
    sum=0
    for i in range(p):
        sum=sum+exp(hk[i])
    try:
        for i in range(p):
            hk[i] =exp(hk[i])/sum
    except:
        return hk
    return hk
def additionBious(w,n):
    for i in range(n):
        w[i]=w[i]+bious
    return w
def rnadomWightGenerator():
    wij = np.zeros((n, m), dtype='float')
    wjk = np.zeros((m, o), dtype='float')
    wkl = np.zeros((o,p), dtype='float')
    for i in range(n):
        for j in range(m):
            wij[i][j]=(float(format(uniform(.1, .9), '.3f')))
    for i in range(m):
        for j in range(o):
            wjk[i][j]=(float(format(uniform(.1, .9), '.3f')))
    for i in range(o):
        for j in range(p):
            wkl[i][j]=(float(format(uniform(.1, .9), '.3f')))
    forwardPass(wij,wjk,wkl)

n=13
m=3
o=3
p=2
bious=1
learningRate=-0.01
input=[.1,.2,.7,.8,.45,-.64,.32,.1,.2,-.7,.8,-.45,-.64]
y=[0.0,1.0]
rnadomWightGenerator()



