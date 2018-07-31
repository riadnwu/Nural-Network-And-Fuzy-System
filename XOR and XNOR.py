from math import exp

def ForwardFacc(w,i1,i2,to1):
    count=0
    c=0
    while True:
        nh1=(i1*w[0]+i2*w[1]+b1*n)
        h1=(1/(1+exp(-nh1)))
        nh2 = (i1 * w[2] + i2 * w[3] + b1 * n)
        h2 = (1 / (1 + exp(-nh2)))

        no1 = (h1 * w[4] + h2 * w[5] + b2 * n)
        o1 = (1 / (1 + exp(-no1)))

        if float(format(o1, '.2f')) != to1:
            e1=.5*pow((to1-o1),2)
            c+=1

        te=e1
        #print "Output o1:"+format(o1, '.2f')

        if(c == 1 ):
            w=BackwardFacc(w,i1,i2,h1,h2,to1,o1)
            c=0
        else:
            return format(o1, '.2f'),count
        count+=1

def BackwardFacc(w,i1,i2,h1,h2,to1,o1):
    w1=[]
    w1.append(w[0] + (n1 * ((-(to1 - o1) * w[4] *( o1*(1-o1))) * (h1 * (1 - h1)) * i1)))
    w1.append(w[1] + (n1 * ((-(to1 - o1) * w[4] *( o1*(1-o1)))  * (h1 * (1 - h1)) * i2)))

    w1.append(w[2] + (n1 * ((-(to1 - o1) * w[5] * (o1 * (1 - o1))) * (h2 * (1 - h2)) * i1)))
    w1.append(w[3] + (n1 * ((-(to1 - o1) * w[5] * (o1 * (1 - o1))) * (h2 * (1 - h2)) * i2)))

    w1.append(w[4] + (n1*((-(to1-o1))*  ( o1*(1-o1)) * (h1))))
    w1.append(w[5] +(n1*((-(to1-o1))* ( o1*(1-o1)) * (h2))))

    return  w1

i1=[0,0,1,1]
i2=[0,1,0,1]
xOr=[0,1,1,0]
xNor=[1,0,0,1]
w=[0.15,0.20,0.25,0.30,0.40,0.45]

b1=0.35
b2=0.60
n=1.0
n1=-.05

print "XOR:\t Steps"
for i in range(4):
    print ForwardFacc(w, i1[i], i2[i], xOr[i])
print "\nXNOR:\t Steps"
for i in range(4):
    print ForwardFacc(w, i1[i], i2[i], xNor[i])