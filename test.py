from data_gen import wav_2_ph
from agent import Agent
from models import  BGRU_Model2

savefile='test5'
batch_size = 10000
Agent = Agent(BGRU_Model2)
Agent.load(savefile)
tst_data = wav_2_ph('files\TIMIT\TEST')

for t in Agent.test(tst_data[:100]):
    print ( t ) 
print(Agent.get_accuracy(tst_data,batch_size=10000))