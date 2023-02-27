import tensorflow as tf
import logging
# disable tf warnings
tf.get_logger().setLevel(logging.ERROR)
from tensorflow.python.keras import Sequential
# For layers
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import InputLayer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Phishing_Detection_Model:
    def __init__(self,num_features,load_weights=False,weights_path="phishing-detection-model.hf",train=True):
        self.load_weights = load_weights
        self.weights_path = weights_path
        self.learning_rate = 2e-4
        self.train_ = train
        self.num_features = num_features
        self.model = self.build_model()
    def build_model(self):
        model=Sequential(name="Phishing_Detection_Model")
        model.add(InputLayer(input_shape=(self.num_features), name='Input_Layer')) 
        model.add(Dense(100,activation='relu', name='Hidden_Layer1'))
        model.add(Dense(200,activation='relu', name='Hidden_Layer2'))
        model.add(Dense(100,activation='relu', name='Hidden_Layer3'))
        model.add(Dense(50, activation='relu', name='Hidden_Layer4')) 
        model.add(Dense(1, activation='sigmoid', name='Output_Layer')) 
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        if self.load_weights:
           model.load_weights(self.weights_path)
        return model

    def train(self, train_feature_vecs, train_answers_vec):
        if self.train_:
            history = self.model.fit(
                x=train_feature_vecs,
                y=train_answers_vec,
                validation_split=0.25,
                shuffle=True,
                epochs=50
            )
        self.model.save("../API/phishing-detection-model")
        self.plot_stats(history)
    def predict(self, test_feature_vecs):
        return self.model.predict(test_feature_vecs)
        
    def plot_stats(self, history):
        accuracy = history.history["accuracy"]
        loss = history.history["loss"]
        epochs = range(1, len(accuracy) + 1)

        plt.title('Training accuracy and loss')
        plt.plot(epochs, accuracy, 'b*', label='Training accuracy')
        plt.plot(epochs, loss, 'b-', label='Training loss')
        plt.legend()
        plt.xlabel("Epochs")
        plt.savefig('Training accuracy and loss')


def calculate_accuracy(predictions, targets):
    correct = 0
    total = 0
    for i in range(len(predictions)):
        act_label = targets[i]
        pred_label = 0 if predictions[i] < 0.5 else 1
        if(act_label == pred_label):
            correct += 1
        total += 1
    accuracy = (correct/total)
    return accuracy

def get_features_targets(df, column):
    targets = df[column]
    targets = tf.convert_to_tensor(targets)
    features = df.drop(columns=column)
    features = tf.convert_to_tensor(features)
    return features, targets

def train_test_split(df, column):
    # train - 60%
    train = df.sample(frac = 0.8)
    # validation - 20% , test - 20%
    test = df.drop(train.index)
    train_features, train_targets = get_features_targets(train, column)
    test_features, test_targets = get_features_targets(test, column)
    return train_features, train_targets, test_features, test_targets 

data = pd.read_csv('phishing_dataset.csv')
df = pd.DataFrame(data)
train_features, train_targets, test_features, test_targets = train_test_split(df,'ClassLabel')

model = Phishing_Detection_Model(num_features=train_features.shape[1])

model.train(train_features,train_targets)

predicted_labels = model.predict(test_features)
acc = calculate_accuracy(predictions=predicted_labels, targets=test_targets)
print(acc)