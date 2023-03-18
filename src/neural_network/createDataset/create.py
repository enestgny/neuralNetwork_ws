import numpy as np
import pandas as pd

# Define the number of samples to generate
num_samples = 3000

# Generate the features  Iris-setosa
sepal_length_setosa = np.random.normal(loc=5, scale=0.3524896872134513, size=num_samples)
sepal_width_setosa = np.random.normal(loc=3.4, scale=0.38102439795469095, size=num_samples)
petal_length_setosa = np.random.normal(loc=1.5, scale= 0.17351115943644546, size=num_samples)
petal_width_setosa = np.random.normal(loc=0.25, scale=0.10720950308167838, size=num_samples)

# Generate the features  Iris-versicolor
sepal_length_versicolor = np.random.normal(loc=5.9, scale=0.5161711470638634, size=num_samples)
sepal_width_versicolor = np.random.normal(loc=2.75, scale=0.3137983233784114, size=num_samples)
petal_length_versicolor = np.random.normal(loc=4.30, scale=0.46991097723995795, size=num_samples)
petal_width_versicolor = np.random.normal(loc=1.30, scale=0.19775268000454405, size=num_samples)

# Generate the features  Iris-virginica
sepal_length_virginica = np.random.normal(loc=6.5, scale=0.6358795932744321, size=num_samples)
sepal_width_virginica = np.random.normal(loc=3.0, scale=0.32249663817263746, size=num_samples)
petal_length_virginica = np.random.normal(loc=5.6, scale=0.5518946956639834, size=num_samples)
petal_width_virginica = np.random.normal(loc=2.00, scale=0.27465005563666733, size=num_samples)



# Generate the labels
species = np.random.choice(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], size=num_samples)

#generate the IDs
ids = np.arange(num_samples)
ids2 = np.arange(start=3000,stop=6000)
ids3 = np.arange(start=6000,stop=9000)
# Combine the features and labels into a Pandas DataFrame for Iris-setosa
iris_data = pd.DataFrame({'Id': ids,
                          'SepalLengthCm': sepal_length_setosa,
                          'SepalWidthCm': sepal_width_setosa,
                          'PetalLengthCm': petal_length_setosa,
                          'PetalWidthCm': petal_width_setosa,
                          'Species': 'Iris-setosa',})

# Combine the features and labels into a Pandas DataFrame for Iris-versicolor
iris_data2 = pd.DataFrame({'Id': ids2,
                          'SepalLengthCm': sepal_length_versicolor,
                          'SepalWidthCm': sepal_width_versicolor,
                          'PetalLengthCm': petal_length_versicolor,
                          'PetalWidthCm': petal_width_versicolor,
                          'Species': 'Iris-versicolor'})

# Combine the features and labels into a Pandas DataFrame for Iris-verginica
iris_data3 = pd.DataFrame({'Id': ids3,
                          'SepalLengthCm': sepal_length_virginica,
                          'SepalWidthCm': sepal_width_virginica,
                          'PetalLengthCm': petal_length_virginica,
                          'PetalWidthCm': petal_width_virginica,
                          'Species': 'Iris-virginica'})
result = pd.concat([iris_data,iris_data2,iris_data3])

result.to_csv('Iris.csv', index=False)
