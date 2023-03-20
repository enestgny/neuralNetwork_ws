from train import Definition
from train import Train
import joblib

path = '/home/enes'

class test():
    def __init__(self,csv):
        self.csv = csv

    def start(self):
        m = 0
        w = joblib.load(path +'/neuralNetwork_ws/src/neural_network/results/weights1.sav')
        w2 = joblib.load(path+'/neuralNetwork_ws/src/neural_network/results/weights2.sav')
        bias = joblib.load(path+'/neuralNetwork_ws/src/neural_network/results/bias1.sav')
        bias2 = joblib.load(path+'/neuralNetwork_ws/src/neural_network/results/bias2.sav')
        Test = Definition(self.csv)                     #Ve sistemimizi tahmin yapabilir duruma getirmiş oluyoruz.
        CSV = Definition(self.csv)
        for k in range(len(Test.Species)):
            K1 = Train(w,bias,CSV.x[k],CSV.Species[k,4])
            aa = K1.ileriYayilim()
            a = K1.ActivationFuncLeakyRelu(aa)
            bbb = Train(w2,bias2,a,CSV.Species[k,4])
            bb = bbb.ileriYayilim()
            b = bbb.ActivationFuncLeakyRelu(bb)

            if   0 < b < 1.4:
                print(k+1,b,'Iris-setosa',Test.x_data[k,5])
                if Test.x_data[k,5] != 'Iris-setosa':  #Hataların olduğunu ve kaç tane olduğunu çıktı olarak göstermesi
                    m += 1
                    print(f'Wrong {m}') 
            elif 1.4 < b < 2.3:
                print(k+1,b,'Iris-versicolor',Test.x_data[k,5])
                if Test.x_data[k,5] != 'Iris-versicolor':
                    m += 1
                    print(f'Wrong {m}') 
            elif 2.3 < b < 4:
                print(k+1,b,'Iris-virginica',Test.x_data[k,5])
                if Test.x_data[k,5] != 'Iris-virginica':
                    m+= 1
                    print(f'Wrong {m}')
        print('Percentage of accurate:',(k-m)*100/k)

