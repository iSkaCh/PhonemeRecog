#Copyright 2018 IskaCh & samelsamel

import random 
import numpy as np
import threading
from sklearn.metrics import accuracy_score

def data_reshape (data):
    ''' Prepares data and labels for training by seperating the data into a time series and reshaping it into a tensor'''
    ph = data [0]
    m = len(ph)%20
    if m > 10 :
        o =np.pad(ph,(0,20-m),'constant',constant_values=0)
    else : 
        o= ph [:len(ph)-m]
    #noise = np.random.randint(-4, 4, o.shape)
    #if random.random() > 0.6 :
        #o+=noise 
    return np.reshape(o,[1,-1,20,1]) , np.reshape(data[1],[1,1,len(data[1])])
class data_generator: 

    def __init__(self,data,batch_size):
        self.data = data
        self.batch_size = batch_size
        self.lock = threading.Lock()
        self.minibatch = random.sample(self.data, self.batch_size)
        self.i=-1
    def __iter__(self):
        return self

    def __next__(self):
        with self.lock:
            self.i+=1
            if self.i == self.batch_size :
                self.i=0
            return data_reshape(self.minibatch[self.i])            
            

class Agent :
    def __init__(self,fun):
        self.learning_rate =0.00001
        self._build_model = fun
        self.model = self._build_model (self)
        self.epochs = 2
     
        
    def train (self,data,batch_size):
        minibatch = random.sample(data, batch_size)# randomly select elements to make the batch
        for ph in minibatch:# train the model with each element from the generated batch
            x,y = data_reshape(ph)
            self.model.fit( x, np.array(y), epochs= self.epochs, verbose=0)            
    def train2 ( self,data,batch_size) : #wont be in report
        self.history=self.model.fit_generator( data_generator(data,batch_size),steps_per_epoch=batch_size,workers=2, epochs= self.epochs, verbose=0)        
    def predict (self,data,single = True):
        if single : 
            x,_ = data_reshape(data)
            return np.argmax(self.model.predict(x)[0] [1])
        else: 
            predictions = []
            for ph in data :
                x,_ = data_reshape(ph)
                predictions.append( np.argmax(self.model.predict(x)[0] [1]))
            return predictions
    def test (self,data):
        for ph in data :
            yield [self.predict(ph),np.argmax(ph[1])]
    def get_accuracy (self, data,batch_size = None) :
        
        if batch_size == None:           
            predictions = self.predict(data,single=False)
            ph_val = np.argmax( [ph[1] for ph in data ], axis= 1) 
            return accuracy_score( predictions,ph_val)
        else :
            minibatch = random.sample(data, batch_size)
            predictions = self.predict(minibatch,single=False)
            ph_val = np.argmax( [ph[1] for ph in minibatch], axis= 1) 
            return accuracy_score( predictions,ph_val)               
    def save(self, name):
        self.model.save_weights(name)
    def load(self, name):
        self.model.load_weights(name)    
