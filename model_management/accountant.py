import pandas as pd
import pickle


primary_class = None
image_size = None
objective = None
direct = False
train_epochs = 10
batch_size = 32
parent_model = None
name = None
model = None
optimizer = None
criterion = None
accuracy_history_train = []
accuracy_history_val = []
extra_history = []
evaluate = False
retrain_name = None

def print_accountant():
    print('Primary Class', primary_class)
    print('Image Size', image_size)
    print('Batch Size', batch_size)
    print('Parent Mode', parent_model)
    print('Name', name)
    print('Evaluate', evaluate)

def add_accuracy(accuracy, state):
    if(state == 'val'):
        accuracy_history_val.append(accuracy)
    else:
        accuracy_history_train.append(accuracy)
def add_extra(extra):
    extra_history.append(extra)
def load_accountant(file, should_evaluate = False, retrain = None):
    global evaluate
    global retrain_name
    if(should_evaluate):
        evaluate = True
    if(retrain is not None):
        retrain_name = retrain
    f = open(file, "r").read()
    exec(f, globals())
    print_accountant()

def save_history(file):
    with open(file, 'wb') as fp:
        pickle.dump({'train':accuracy_history_train, 'val': accuracy_history_val, 'extra':extra_history}, fp)