from keras.models import Sequential
from keras.layers import Conv1D,Dense,TimeDistributed,GlobalMaxPooling1D,BatchNormalization,CuDNNLSTM,CuDNNGRU,Bidirectional,MaxPooling1D
from keras.constraints import maxnorm
from keras.optimizers import Adam
from keras.layers import Flatten

def BGRU_Model2 (self) :
    model = Sequential()  
    
    model.add(TimeDistributed(Conv1D(40,14,kernel_initializer='random_uniform',padding = 'same', activation='relu',kernel_constraint=maxnorm(1000),name="cnn_0"),input_shape=( None,20,1)))
    model.add(TimeDistributed(Conv1D(120,3,kernel_initializer='random_uniform',activation='relu',kernel_constraint=maxnorm(1000),name="cnn_1")))        
    model.add(TimeDistributed(MaxPooling1D(pool_size=3)))
    
    model.add(TimeDistributed(Flatten()))
    model.add(Bidirectional(CuDNNGRU(120, return_sequences=True)))
    model.add(Dense(65, activation='softmax',name="dense_1"))
    model.compile(loss='categorical_crossentropy',
                      optimizer=Adam(lr=self.learning_rate))    
    return model 
def BLSTM_Model (self) :
    model = Sequential()
   
    model.add(TimeDistributed(Conv1D(40,14,kernel_initializer='random_uniform',padding = 'same', activation='relu',kernel_constraint=maxnorm(1000),name="cnn_0"),input_shape=( None,20,1)))
    model.add(TimeDistributed(Conv1D(120,3,kernel_initializer='random_uniform',activation='relu',kernel_constraint=maxnorm(1000),name="cnn_1")))        
    model.add(TimeDistributed(MaxPooling1D(pool_size=3)))
    
    model.add(TimeDistributed(Flatten()))
    model.add(Bidirectional(CuDNNLSTM(120, return_sequences=True)))
    model.add(Dense(65, activation='softmax',name="dense_1"))
    model.compile(loss='categorical_crossentropy',
                  optimizer=Adam(lr=self.learning_rate))    
    return model 

def GRU_Model (self) :
    model = Sequential()
    
    model.add(TimeDistributed(Conv1D(30,7,kernel_initializer='random_uniform',padding = 'same', activation='relu',kernel_constraint=maxnorm(10),name="cnn_0"),input_shape=( None,20,1)))
    model.add(TimeDistributed(Conv1D(100,4,kernel_initializer='random_uniform',activation='relu',kernel_constraint=maxnorm(10),name="cnn_1")))        
    model.add(TimeDistributed(GlobalMaxPooling1D()))
    model.add(CuDNNGRU(160, return_sequences=True))
    model.add(Dense(65, activation='softmax',name="dense_1"))
    model.compile(loss='categorical_crossentropy',
                      optimizer=Adam(lr=self.learning_rate))    
    return model 