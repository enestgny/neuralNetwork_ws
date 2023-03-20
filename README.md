
# Neural Network - Iris

Iris-setosa,Iris-versicolor ve Iris-virginica çiçek türlerinin boyutlarını kullanarak tür tahmini yapar.


```bash
  git clone https://github.com/enestgny/neuralNetwork_ws.git
```
## Dataset oluşturma
Model için istediğimiz genişlikte dataset oluşturabilmek için:

```bash
  cd neuralNetwork_ws/src/neural_network/createDataset
  python3 create.py
```
her bir çiçek türü için girmek istediğimiz miktar, num_samples değeri değiştirilerek elde edilir.

## Eğitim

```bash
  cd ..
  cd scripts/
  python3 split.py
```
dataseti train ve test olarak ikiye ayırır ve train işlemini başlatır. Ağırlıkların güncellenmesi ile birlikte test aşamasına geçiş yapılır.

## Test

```bash
  python3 first.py
  python3 second.py
```
farklı terminallerde açıldığında iki ayrı python dosyasının iletişim halinde olduğu görülür.