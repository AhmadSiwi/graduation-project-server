import numpy as np
import librosa
import tflearn

#path = "data/quraan/12-1-3.wav"

def mfcc_batch_generator(path):
  batch_features = []
  wave, sr = librosa.load(path, mono=True)
  mfcc = librosa.feature.mfcc(wave, sr)
  mfcc = np.pad(mfcc,((0,0),(0,1500-len(mfcc[0]))), mode='constant', constant_values=0)
  batch_features.append(np.array(mfcc))
  return batch_features

learning_rate = 0.00002
#batch_size = 256

width = 20
height = 1500
classes = 21

#X = mfcc_batch_generator(path)

net = tflearn.input_data([None, width, height])
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, classes, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_verbose=3)
model.load("tflearn.lstm.model")

def predict(path):
  X = mfcc_batch_generator(path)
  _y=model.predict(X)
  y = np.argmax(_y[0])
  if (y<6):
    return "1-"+str(y+2)
  elif (y<10):
    y -= 6
    return "112-"+str(y+1)
  elif (y<15):
    y -= 10
    return "113-"+str(y+1)
  else:
    y -= 15
    return "114-"+str(y+1)

