import pandas as pd
import numpy as np
from emit import emittance_calc
import matplotlib.pyplot as plt



df=pd.read_excel("indata.xlsx")


c=emittance_calc()
c.energy=df["束流能量(MeV)"][0]
c.Lq=df["透镜有效长度/Q铁有效长度Lq(m)"][0]
c.Ld=df["透镜出口到截面靶的距离/漂移段长度Ld(m)"][0]
ks=np.array(df["聚焦参数k"].to_list())
sig2f=np.array(df["束斑尺寸σ^2（聚焦方向）"].to_list())
sig2d=np.array(df["束斑尺寸σ^2（散焦方向）"].to_list())
ef,eaf,ebf,ecf,enxf,ems=c.sol_f(ks,sig2f)
ed,ead,ebd,ecd,enxd,ems=c.sol_d(ks,sig2d)
columns=["聚焦发射度ε","聚焦Twiss_α","聚焦Twiss_β","聚焦Twiss_γ","散焦发射度ε","散焦Twiss_α","散焦Twiss_β","散焦Twiss_γ"]
data=[[ef,eaf,ebf,ecf,ed,ead,ebd,ecd]]
print(data)
dfo=pd.DataFrame(data=data,columns=columns)
dfo.to_excel("outdata.xlsx")


##FIGF
betae,alphae,gammae=ebf*ef,eaf*ef,ecf*ef
print(betae,alphae,gammae)
fittedf=[c.func_f(x,betae,alphae,gammae) for x in ks]
plt.plot(ks,fittedf,label="聚焦发射度拟合")
plt.scatter(ks,sig2f)
plt.savefig("聚焦发射度拟合结果.png")
plt.clf()
##FIGD
betae,alphae,gammae=ebd*ed,ead*ed,ecd*ed
print(betae,alphae,gammae)
fittedd=[c.func_d(x,betae,alphae,gammae) for x in ks]
plt.plot(ks,fittedd,label="散焦发射度拟合")
plt.scatter(ks,sig2d)
plt.savefig("散焦发射度拟合结果.png")
plt.clf()