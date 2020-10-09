#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
#Factor de potencia unitario
PSIL = 2200.5; #MW

V2_pu=[1.0738, 1.0737, 1.0733, 1.0727, 1.0718, 1.0706, 1.0692, 1.0675, 1.0655, 1.0632, 1.0606, 1.0578, 1.0546, 1.0510, 1.0472,
1.0429, 1.0383, 1.0332, 1.0277, 1.0216, 1.0151, 1.0079, 1.0000, 0.9914, 0.9820, 0.9714, 0.9597, 0.9465, 0.9313, 0.9135, 0.8919,
0.8635, 0.8184];

P2=[0, 0.04544421722, 0.09088843445, 0.1363326517, 0.1817768689, 0.2272210861, 0.2726653033, 0.3181095206, 0.3635537378,
0.408997955, 0.4544421722, 0.4998863895, 0.5453306067, 0.5907748239, 0.6362190411, 0.6816632584, 0.7271074756, 0.7725516928,
0.81799591, 0.8634401272, 0.9088843445, 0.9543285617, 0.9997727789, 1.045216996, 1.090661213, 1.13610543, 1.181549648,
1.226993865, 1.272438082, 1.317882299, 1.363326517, 1.408770734, 1.454214951];


# In[11]:


#plotear el grafico
plt.plot(P2, V2_pu);
plt.scatter(P2, V2_pu)
xlab = "Potencia activa (p.u)"
ylab = "Tension en p.u"
titulo = "Curva PV a fp unitario"
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(titulo)
#introducir texto
plt.text(1.0,1.0, "SIL Operation")


# In[24]:


#Factor de potencia 0.9 en adelanto

V2_adelanto = [1.0738, 1.0816, 1.0891, 1.0963, 1.1031, 1.1096, 1.1158, 1.1218, 1.1275, 1.1329, 1.1380, 1.1430, 1.1476,
1.1521, 1.1563, 1.1602, 1.1640, 1.1675, 1.1708, 1.1739, 1.1768, 1.1794, 1.1818, 1.1840, 1.1860, 1.1877, 1.1892, 1.1905,
1.1915, 1.1923, 1.1928, 1.1931, 1.1931, 1.1927, 1.1921, 1.1912, 1.1899, 1.1882, 1.1862, 1.1837, 1.1807,1.1772, 1.1731,
1.1683, 1.1628, 1.1563, 1.1486, 1.1396, 1.1287, 1.1287, 1.1150, 1.0971, 1.0698, 1.0280]


P2_adelanto =[0, 0.04544421722, 0.09088843445, 0.1363326517, 0.1817768689, 0.2272210861, 0.2726653033, 0.3181095206,
0.3635537378, 0.408997955, 0.4544421722, 0.4998863895, 0.5453306067, 0.5907748239, 0.6362190411, 0.6816632584, 0.7271074756,
0.7725516928, 0.81799591, 0.8634401272, 0.9088843445, 0.9543285617, 0.9997727789, 1.045216996, 1.090661213, 1.136105431,
1.181549648, 1.226993865, 1.272438082, 1.317882299, 1.363326517, 1.408770734, 1.454214951, 1.499659168, 1.545103386, 1.590547603,
1.63599182, 1.681436037, 1.726880254, 1.772324472,1.817768689,1.863212906, 1.908657123, 1.954101341, 1.999545558, 2.044989775,
2.090433992, 2.135878209, 2.181322427, 2.181322427, 2.226766644, 2.272210861, 2.317655078, 2.363099296]


# In[30]:


#plotear el grafico
plt.plot(P2_adelanto, V2_adelanto);
plt.scatter(P2_adelanto, V2_adelanto)
xlab = "Potencia activa (p.u)"
ylab = "Tension en p.u"
titulo = "Curva PV a fp adelanto 0.9"
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(titulo)
#introducir texto
plt.text(1.0,1.1818, "SIL")


# In[27]:


plt.plot(P2_adelanto, V2_adelanto);
plt.scatter(P2_adelanto, V2_adelanto)
plt.scatter(P2, V2_pu)
plt.plot(P2, V2_pu);


# In[34]:


#factor de potencia 0.95 adelanto

V_fpadel = [1.0738, 1.0791, 1.0841, 1.0888, 1.0932, 1.0974, 1.1013, 1.1049, 1.1083, 1.1114, 1.1143, 1.1170, 1.1194, 1.1216, 
            1.1235, 1.1252,1.1267, 1.1279, 1.1289, 1.1296, 1.1301, 1.1303, 1.1303, 1.1299, 1.1293, 1.1284, 1.1272, 1.1257,
            1.1238, 1.1215, 1.1189, 1.1158, 1.1123, 1.1082, 1.1036, 1.0984, 1.0925, 1.0857, 1.0779, 1.0689, 1.0585, 1.046,
            1.0307, 1.0109,0.9817, 0.9024]

P_2adel = [0, 0.04544421722, 0.09088843445, 0.1363326517, 0.1817768689, 0.2272210861, 0.2726653033, 0.3181095206, 0.3635537378,
           0.408997955, 0.4544421722, 0.4998863895, 0.5453306067, 0.5907748239, 0.6362190411, 0.6816632584, 0.7271074756,
           0.7725516928, 0.81799591, 0.8634401272, 0.9088843445, 0.9543285617, 0.9997727789, 1.045216996, 1.090661213,
           1.136105431, 1.181549648, 1.226993865, 1.272438082, 1.317882299, 1.363326517, 1.408770734, 1.454214951, 1.499659168,
           1.545103386, 1.590547603, 1.63599182, 1.681436037, 1.726880254, 1.772324472, 1.817768689, 1.863212906, 1.908657123,
           1.954101341, 1.999545558, 2.044989775]


# In[37]:


#plotear el grafico
plt.plot(P_2adel, V_fpadel);
plt.scatter(P_2adel, V_fpadel)
xlab = "Potencia activa (p.u)"
ylab = "Tension en p.u"
titulo = "Curva PV a fp adelanto 0.9"
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(titulo)
#introducir texto
#plt.text(1.0,1.1818, "SIL")


# In[39]:


title="Curva PV superior de linea de transmision transpuesta"
xtit = "Potencia activa(P.U)"
y_tit = "Tension en la linea (P.U)"


#Grafico final
plt.plot(P2_adelanto, V2_adelanto);
plt.plot(P2, V2_pu);
plt.plot(P_2adel, V_fpadel)
plt.scatter(P_2adel, V_fpadel)
plt.scatter(P2_adelanto, V2_adelanto)
plt.scatter(P2, V2_pu)

#customize
plt.title(title)
plt.xlabel(xtit)
plt.ylabel(y_tit)

