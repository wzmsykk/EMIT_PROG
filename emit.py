import numpy as np
from numpy import ndarray
from numpy import cos,cosh,sin,sinh,sqrt
from scipy import linalg
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
class emittance_calc:
    def __init__(self):
        self.ks=1 ###聚焦参数
        self.Lq=0.1 ###透镜有效长度，Q铁有效长度(m)
        self.Ld=1.4528 ###透镜出口到截面靶的距离,漂移段长度(m)
        self.sigma2=1 ###束斑尺寸平方
        self.energy=53.4 ###束流能量(MeV)
        pass
    def func_f(self,xdata,*opt): ###聚焦
        k,Lq,Ld=xdata,self.Lq,self.Ld
        betae,alphae,gammae=opt
        r11=cos(sqrt(k)*Lq)-sqrt(k)*Ld*sin(sqrt(k)*Lq)
        r12=1.0/sqrt(k)*sin(sqrt(k)*Lq)+Ld*cos(sqrt(k)*Lq)
        y=betae*r11**2-2*alphae*r11*r12+gammae*r12**2
        return y
    def func_d(self,xdata,*opt): ###散焦
        k,Lq,Ld=xdata,self.Lq,self.Ld
        betae,alphae,gammae=opt
        R11=cosh(sqrt(k)*Lq)+sqrt(k)*Ld*sinh(sqrt(k)*Lq) 
        R12=1/sqrt(k)*sinh(sqrt(k)*Lq)+Ld*cosh(sqrt(k)*Lq)
        y=betae*R11**2+alphae*-2*R11*R12+gammae*R12**2
        return y
    def sol_f(self,ks,sigma2):    
        ###ks 聚焦参数
        ###sigma2 束斑尺寸平方
        ydata=sigma2
        xdata=ks
        init=[1.0,1.0,1.0]
        result=curve_fit(self.func_f,xdata,ydata,init)
        ems=result[0]
        e=sqrt(ems[0]*ems[2]-ems[1]**2)
        enx=e*(self.energy/0.511)
        eb=ems[0]/e
        ea=ems[1]/e
        ec=ems[2]/e
        return e,ea,eb,ec,enx,ems
    def sol_d(self,ks,sigma2):    
        ###ks 聚焦参数
        ###sigma2 束斑尺寸平方
        ydata=sigma2
        xdata=ks
        init=[1.0,1.0,1.0]
        result=curve_fit(self.func_d,xdata,ydata,init)
        ems=result[0]
        e=sqrt(ems[0]*ems[2]-ems[1]**2)
        enx=e*(self.energy/0.511)
        eb=ems[0]/e
        ea=ems[1]/e
        ec=ems[2]/e
        return e,ea,eb,ec,enx,ems
    
class emittance_calc_solenoid():
    def __init__(self):
        self.ks=1 ###聚焦参数
        self.L=0.1 ###螺线管有效长度(m)
        self.Ld=1.4528 ###螺线管漂移段长度(m)
        self.sigma2=1 ###束斑尺寸平方
        self.energy=53.4 ###束流能量(MeV)
        pass
    
##########计算螺线管的束流发射度
    def func_f(self,xdata,*opt): ###聚焦
        betae,alphae,gammae=opt
        S=sin(self.ks*self.L)
        C=cos(self.ks*self.L)
        R11=C-self.ks*self.Ld*S
        R12=1/self.ks*S+self.Ld*C
        y=betae*R11**2+alphae*-2*R11*R12+gammae*R12**2
        
    def sol_f(self,ks,sigma2):    
        ###ks 聚焦参数
        ###sigma2 束斑尺寸平方
        ydata=sigma2
        xdata=ks
        init=[1.0,1.0,1.0]
        result=curve_fit(self.func_f,xdata,ydata,init)
        ems=result[0]
        e=sqrt(ems[0]*ems[2]-ems[1]**2)
        enx=e*(self.energy/0.511)
        eb=ems[0]/e
        ea=ems[1]/e
        ec=ems[2]/e
        return e,ea,eb,ec,enx,ems
if __name__ =="__main__":
    c=emittance_calc()

    ##c.ks=np.array([3.13,3.15,3.17,3.19,3.21,3.23,3.25,3.27])
    ##c.ks=np.array([3.05,3.07,3.09,3.11,3.13,3.15,3.17,3.19,3.21,3.23,3.25,3.27])
    ks=np.array([20.4,20.5,20.6,20.7,20.8,20.9,21.0,21.1,21.2,21.3,21.4,21.5])  ###XDATA
    ##c.sigma=np.array([0.108,0.009,0.0086,0.0093,0.0114,0.0144,0.0185,0.0228])
    sigma2=np.array([0.03,0.023,0.017,0.015,0.0108,0.009,0.0086,0.0093,0.0114,0.0144,0.0185,0.0228]) ###YDATA
    sigma=np.array([0.17320508,0.15165751,0.13038405,0.12247449,0.10392305,0.09486833,0.09273618,0.09643651,0.10677078,0.12,0.13601471,0.15099669]) 
    plt.scatter(ks,sigma2)

    #####REF FIT MATLAB
    beta,alpha,gamma=(23.9179,-35.0021,51.2648)
    e=0.107006
    betae,alphae,gammae=beta*e,alpha*e,gamma*e
    fitted=[c.func_f(x,betae,alphae,gammae) for x in ks]
    plt.plot(ks,fitted,label="MAT")

    #####FIT PYHTON
    e,ea,eb,ec,enx,ems=c.sol_f(ks,sigma2)
    betae,alphae,gammae=ems[0],ems[1],ems[2]
    beta,alpha,gamma=(23.917880340739202,-35.002063304277634,51.264761679912475)
    e=0.10700617620847394
    betae,alphae,gammae=beta*e,alpha*e,gamma*e
    print(ems,[betae,alphae,gammae])
    fitted2=[c.func_f(x,betae,alphae,gammae) for x in ks]
    plt.plot(ks,fitted2,label="PY")


    plt.legend()
    plt.show()