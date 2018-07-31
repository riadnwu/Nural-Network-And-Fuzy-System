

def PercepTion (w,z):
    x=[0,0,1,1]
    y=[0,1,0,1]
    l=-1
    for i in range(4):
        print "For x: "+`x[i]`+" y: "+`y[i]`+" z: "+`z[i]`
        WaightChack(w,l,x[i],y[i],z[i])
        print "________________________________"


def WaightChack(w,l,x,y,z):
    if (l * w[0]) + (x * w[1]) + (y * w[2]) < 0:
        if (z != 0):
            print "Not Match!! Value:0 != z:1\n"
            data = [l, x, y]
            t=0
            NewWaight(w, data, z,t)
        else:
            print "Value Match: Value: 0 == z: 0\n"

    elif (l * w[0]) + (x * w[1]) + (y * w[2]) > 0:
        if (z != 1):
            print "Not Match!! Value: 1 != z: 0\n"
            data=[l,x,y]
            t=1
            NewWaight(w,data,z,t)
        else:
            print "Value Match: Value: 1 == z: 1\n"

def NewWaight(w,data,z,m):
    N = .20
    tw = [0, 0, 0]
    for i in range(3):
       tw[i] = w[i] + N * (z - m) * data[i]
    print"New Waight: w0:"+`tw[0]`+" w1:"+`tw[1]`+" w2:"+`tw[2]`+"\n"
    WaightChack(tw,data[0],data[1],data[2], z)

#Main Function
w=[.3,.5,-.4]
and1=[0,0,0,1]
or1=[0,1,1,1]
nAnd=[1,1,1,0]
nOr=[1,0,0,0]
#xOr=[0,1,1,0]
#xNor=[1,0,0,1]

print("Perceptron for AND\n")
PercepTion(w,and1)
print("\n\nPerceptron for OR\n")
PercepTion(w,or1)
print("\n\nPerceptron for NAND\n")
PercepTion(w,nAnd)
print("\n\nPerceptron for NOR\n")
PercepTion(w,nOr)
'''print("\n\nPerceptron for XOR\n")
PercepTion(w,xOr)
print("\n\nPerceptron for XNOR\n")
PercepTion(w,xNor)'''


