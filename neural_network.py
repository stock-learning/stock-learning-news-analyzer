# Author: Carlos Henrique Ponciano da Silva
from keras import models
from keras import layers
from keras.layers import Dense


# create a new model from scratch
# model tensorflow neural network for data classification
def build(n_input):
    model = models.Sequential()
    model.add(layers.Embedding(n_input, 16))
    model.add(layers.GlobalAveragePooling1D())
    model.add(layers.Dense(16, activation = "relu"))
    model.add(layers.Dense(1, activation="sigmoid")) 
    model.summary()
    return model

# loads a model already exist in memory
def load():
    return models.load_model(f'models/model')