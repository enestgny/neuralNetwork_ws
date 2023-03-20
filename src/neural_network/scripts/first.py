#!/usr/bin/env python
import pandas as pd
import numpy as np
import rospy
from std_msgs.msg import Float64MultiArray
import joblib

m = 0
path = '/home/enes'
joblib.dump(m,path+'/neuralNetwork_ws/src/neural_network/results/m.sav')

class ReturnValue():                      #İstediğmiz herhangi bir csv dosyasını rahat bir şekilde okuyabilmek için
    def __init__(self):
        self.data = None
        self.Species = None
        self.CSV = self.Definition(path+'/neuralNetwork_ws/src/neural_network/csv/test.csv')

    def Definition(self, a):
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
        return Species #Returnde class yazarak fonksiyondan birden çok çıktı alabiliyoruz.

    def talker(self):
        pub1= rospy.Publisher('chatter_v1',Float64MultiArray, queue_size=10)
        rate = rospy.Rate(100) # 10hz
        data3 = Float64MultiArray()
        for i in range(len(self.CSV)):
            print(i)
            print(self.CSV[i])
            data3.data= np.array(self.CSV[i],dtype=np.float32)
            pub1.publish(data3)
            rate.sleep()
        

if __name__ == '__main__':
    rospy.init_node('first', anonymous=True)
    enes = ReturnValue()
    rate = rospy.Rate(60)
    while not rospy.is_shutdown():
        enes.talker()
        rate.sleep()
    