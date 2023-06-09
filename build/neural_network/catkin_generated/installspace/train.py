#!/usr/bin/env python3
from matplotlib import pyplot as plt #Grafik oluşturmak için
import numpy as np
import pandas as pd
import joblib

plot_x2 = []
plot_y2 = []



class ReturnValue():                      #İstediğmiz herhangi bir csv dosyasını rahat bir şekilde okuyabilmek için
    def __init__(self,data,x_data,Species,x):
        self.data = data
        self.Species = Species
        self.x = x
        self.x_data =x_data

def Definition(a):
    data = pd.read_csv(a)
    x_data = np.array(data)# Csv dosyasından alınan datayı array şeklinde numpy ile düzenliyoruz
    Species = np.delete(x_data,0,1)#[0]:SepalLengthCm, [1]:SepalWidthCm, [2]:PetalLengthCm, [3]:PetalWidthCm, [4]: Species

    for j in range(len(Species)):  #Matris içindeki string verileri backward işleminde kullanabilmek için int verilere çeviriyoruz.
        if Species[j,4] == 'Iris-setosa':
            Species[j,4] = 1
        elif Species[j,4] == 'Iris-versicolor':
            Species[j,4] = 2
        elif Species[j,4] == 'Iris-virginica':
            Species[j,4] = 3
    x = np.delete(Species,4,1)#[0]:SepalLengthCm, [1]:SepalWidthCm, [2]:PetalLengthCm, [3]:PetalWidthCm
    return ReturnValue(data,x_data,Species,x) #Returnde class yazarak fonksiyondan birden çok çıktı alabiliyoruz.

class Train():
    def __init__(self,weight,bias,data,yDegeri):
        self.weight = weight
        self.bias = bias
        self.data = data
        self.yDegeri = yDegeri
     #aktivasyon fonksiyonları

    def ActivationFuncTanh(self,zfunce):
        re = (2/(1+ np.exp((-2)*float(zfunce)))) -1
        re = np.tanh(float(zfunce))
        return re
    
    def ActivationFuncRelu(self,zfunce):
        if zfunce  >= 0:
            re = zfunce
        elif zfunce < 0:
            0 
        return re
    
    def ActivationFuncLeakyRelu(self,zfunce):
        if zfunce.any()  >= 0:
            re = zfunce
        elif zfunce.any() < 0:
            re= 0.01*zfunce
        return re
    
    def ActivationFuncSwish(self,zfunce):
        re = zfunce /(1+np.exp(float(-zfunce)))
        return re
    
    #İleri yayılım ve geri yayılımda kullanılan fonksiyonlar
    def ileriYayilim(self):
        z = np.dot(self.weight,self.data) + self.bias
        return z
    
    def derivative(self,L2,R2,X,w2):#Geri yayılımda türevli ifadelerin değerlerinin bulunması
        dZ2 = L2 - self.yDegeri
        dW2 = dZ2.dot(R2.T.reshape(1,3))
        db2 = np.sum(dZ2)
        dZ1 = dZ2.dot(w2)
        dW1 = dZ1.reshape(3,1).dot(X.reshape(1,4))
        db1 = np.sum(dZ1)
        return dW1, db1, dW2, db2
    
    def backward(self,w2,dW1, db1, dW2, db2,b2,w,bias):# Bias ve ağırlık değerlerinin güncellenmesi
        alpha = 0.01
        w = w - alpha * dW1
        bias = bias - alpha * db1    
        w2= w2 - alpha * dW2  
        b2= b2 -  alpha * db2
        return w2,b2,w,bias

    def Error(self,z):
        a = 1/2*(z-self.yDegeri)**2
        return a

class neuralNetwork():
    def __init__(self,csv):
        self.csv = csv
    
    def start(self):
        p=0
        arg = np.random.default_rng(1) #Random sayı üretmek için
        w = arg.random((3,4))
        w2 = arg.random((1,3))
        bias = arg.random()
        bias2 = arg.random()
        CSV = Definition(self.csv)
        for k in range(10):#Çok katmanlıda sadece değerleri döndürmek yetmedi. Döngüyü arttırdığımda hatalı bulduğu değer sayısı azaldı.
            for i in range(len(CSV.data)):              # Tanımladığımız  fonksiyonlara datamızı okutuyoruz.
                p+= 1
                R1 = Train(w,bias,CSV.x[i],CSV.Species[i,4])
                R22 = R1.ileriYayilim()
                R2 = R1.ActivationFuncLeakyRelu(R22)
                L1 = Train(w2,bias2,R2,CSV.Species[i,4])
                L22 = L1.ileriYayilim()
                L2 = L1.ActivationFuncLeakyRelu(L22)
                L3 = L1.Error(L2)
                print(p)
                print('Error',L3)
                dW1, db1, dW2, db2 = R1.derivative(L2,R2,CSV.x[i],w2)
                w2,bias2,w,bias = R1.backward(w2,dW1, db1, dW2, db2,bias2,w,bias)
                plot_x2.append(p) #Grafik oluşturabilmek için değerlerimizi liste şeklinde topluyoruz.
                plot_y2.append(L3)
        plt.title("Value of error function")#Grafiğe isim verme
        plt.plot(plot_x2,plot_y2,color ="red")
        plt.show()
        joblib.dump(w,'/home/enes/neuralNetwork_ws/src/neural_network/results/weights1.sav')
        joblib.dump(w2,'/home/enes/neuralNetwork_ws/src/neural_network/results/weights2.sav')
        joblib.dump(bias,'/home/enes/neuralNetwork_ws/src/neural_network/results/bias1.sav')
        joblib.dump(bias2,'/home/enes/neuralNetwork_ws/src/neural_network/results/bias2.sav')