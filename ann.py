
import numpy as np
X=np.array(([1,9], [3,6], [5,6]), dtype=float)
y=np.array(([98], [34], [65]), dtype=float)
X=X/np.amax(X, axis=0)
y=y/100
def sig(x):
    return 1/(1+ np.exp(-x))
def der_sig(x):
    return x*(1-x)
epoch=7000
lr=0.2
inpn=2
hidn=3
outn=1
wh=np.random.uniform(size=(inpn,hidn))
bh=np.random.uniform(size=(1,hidn))
wout=np.random.uniform(size=(hidn,outn))
bout=np.random.uniform(size=(1,outn))
for i in range(epoch):
    hinp1=np.dot(X,wh)
    hinp=hinp1+bh
    hlayer_act=sig(hinp)
    out1=np.dot(hlayer_act,wout)
    out=out1+bout
    output=sig(out)
    eo=y-output
    outgrad=der_sig(output)
    d_output=eo*outgrad
    eh=d_output.dot(wout.T)
    hidgrad=der_sig(hlayer_act)
    d_hid=eh*hidgrad
    wout+=hlayer_act.T.dot(d_output)*lr
    wh+=X.T.dot(d_hid)*lr
print("input: "+str(X))    
print("actual output: "+str(y))
print("pre out : ",output)    