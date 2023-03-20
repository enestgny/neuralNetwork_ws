#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64MultiArray
from train import Train
import joblib
import numpy as np

path = '/home/enes'

class ReturnValue():
    def __init__(self,withName,b):
        self.withName = withName
        self.b = b

def start(data):
    w = joblib.load(path+'/neuralNetwork_ws/src/neural_network/results/weights1.sav')
    w2 = joblib.load(path+'/neuralNetwork_ws/src/neural_network/results/weights2.sav')
    bias = joblib.load(path+'/neuralNetwork_ws/src/neural_network/results/bias1.sav')
    bias2 = joblib.load(path+'/neuralNetwork_ws/src/neural_network/results/bias2.sav')
    withName = data
    print(withName)
    withoutName = np.delete(withName,4)
    K1 = Train(w,bias,withoutName,withName[-1])
    aa = K1.ileriYayilim()
    a = K1.ActivationFuncLeakyRelu(aa)
    bbb = Train(w2,bias2,a,withName[-1])
    bb = bbb.ileriYayilim()
    b = bbb.ActivationFuncLeakyRelu(bb)
    return ReturnValue(withName,b)

def callback(data):
    m = joblib.load(path+'/neuralNetwork_ws/src/neural_network/results/m.sav')
    result1=data.data
    result = start(result1) 
    print(result.b)
    if   0 < result.b < 1.4:
        print('Result: Iris-setosa ', result.b)
        if result.withName[-1] != 1: #Hataların olduğunu ve kaç tane olduğunu çıktı olarak göstermesi
            m += 1
            print(f'Wrong {m}') 
    elif 1.4 < result.b < 2.3:
        print('Result:Iris-versicolor  ', result.b)
        if result.withName[-1] != 2:
            m += 1
            print(f'Wrong {m}') 
    elif 2.3 < result.b < 4:
        print('Result:Iris-virginica ', result.b)
        if result.withName[-1] != 3:
            m+= 1
            print(f'Wrong {m}')
    joblib.dump(m,path+'/neuralNetwork_ws/src/neural_network/results/m.sav')


def listener():
    rospy.init_node('second', anonymous=True)
    rospy.Subscriber('chatter_v1', Float64MultiArray , callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
