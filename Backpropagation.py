'''
Md. Riadul Islam
riadnwu@gmail.com
'''
from math import exp

'''i1=input("I1:")#0.05
i2=input("I2:")#0.10
w=[]
for i in range(8): #w=[0.15,0.20,0.25,0.30,0.40,0.45,0.50,0.55]
    w.append(input("W"+`i+1`+":"))
b1=input("B1:")#0.35
b2=input("B2:")#0.60
to1=input("O1:")#0.01
to2=input("O2:")#0.99
n=input("N:")#1.0
n1=input("N1:")#-0.5 Input Manually'''

i1=0.05
i2=0.10
w=[]
w=[0.15,0.20,0.25,0.30,0.40,0.45,0.50,0.55]
b1=0.35
b2=0.60
to1=1
to2=1
n=1.0
n1=-0.4

def ForwardFacc(w):
    count=0
    while True:
        nh1=(i1*w[0]+i2*w[1]+b1*n)
        h1=(1/(1+exp(-nh1)))
        nh2 = (i1 * w[2] + i2 * w[3] + b1 * n)
        h2 = (1 / (1 + exp(-nh2)))

        no1 = (h1 * w[4] + h2 * w[5] + b2 * n)
        o1 = (1 / (1 + exp(-no1)))
        no2 = (h1 * w[6] + h2 * w[7] + b2 * n)
        o2 = (1 / (1 + exp(-no2)))
        c=0
        if float(format(o1, '.2f')) != to1:
            e1=.5*pow((to1-o1),2)
            c+=1
        if float(format(o2, '.2f')) != to2:
            e2=.5*pow((to2-o2),2)
            c+=1

        te=e1+e2
        print "Output o1:"+format(o1, '.5f')
        print "Output o2:"+format(o2, '.5f')
        #print `c`
        print "Total Error:"+format(te, '.5f')+"\n"
        if(c == 1 ):
            w=BackwardFacc(w,h1,h2,o1,o2)
            c=1
        elif (c == 2):
            w = BackwardFacc(w, h1, h2, o1, o2)
            c = 0
        else:
            print "\n\nTotal Steaps:"+`count`
            print "Match Output o1:"+format(o1, '.2f')
            print "Match Output o2:" + format(o2, '.2f')
            break
        count+=1

def BackwardFacc(w,h1,h2,o1,o2):
    w1=[]
    w1.append(w[0] + (n1 * (((-(to1 - o1) * w[4] *( o1*(1-o1))) + (- (to2 - o2) * w[6] *(o2*(1 - o2)) )) * (h1 * (1 - h1)) * i1)))
    w1.append(w[1] + (n1 * (((-(to1 - o1) * w[4] *( o1*(1-o1))) + (- (to2 - o2) * w[6] *(o2*(1 - o2)) )) * (h1 * (1 - h1)) * i2)))

    w1.append(w[2] + (n1 * (((-(to1 - o1) * w[5] * (o1 * (1 - o1))) + (- (to2 - o2) * w[7] * (o2 * (1 - o2)))) * (h2 * (1 - h2)) * i1)))
    w1.append(w[3] + (n1 * (((-(to1 - o1) * w[5] * (o1 * (1 - o1))) + (- (to2 - o2) * w[7] * (o2 * (1 - o2)))) * (h2 * (1 - h2)) * i2)))

    w1.append(w[4] + (n1*((-(to1-o1))*  ( o1*(1-o1)) * (h1))))
    w1.append(w[5] +(n1*((-(to1-o1))* ( o1*(1-o1)) * (h2))))

    w1.append(w[6]+ (n1*((-(to2 - o2)) * (o2*(1 - o2)) * (h1))))
    w1.append(w[7]+ (n1*((-(to2 - o2)) * (o2*(1 - o2)) * (h2))))

    return  w1


ForwardFacc(w)

'''input
.05
.10
.15
.20
.25
.30
.40
.45
.50
.55
.35
.60
.01
.99
1.0
-.5
'''