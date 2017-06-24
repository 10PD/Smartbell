from nimblenet.activation_functions import sigmoid_function
from nimblenet.cost_functions import cross_entropy_cost
from nimblenet.learning_algorithms import *
from nimblenet.neuralnet import NeuralNet
from nimblenet.preprocessing import construct_preprocessor, standarize
from nimblenet.data_structures import Instance
from nimblenet.tools import print_test
import random


#Example Training set
#dataset             = [ Instance( [0,0,0], [0,0] ), Instance( [1,1,1], [0,1] ), Instance( [2,2,2], [1,0] ) ]



#Generates example data of N samples
#X is 'slowly moving up/down-wards'
#Y is 'slightly moving side-to-side' for random variance
def example_gen(start, end, iterable=1):
    last_x = list()
    last_y = list()
    for i in range(start, end, iterable):
        rdm = random.randint(-3,3)
        last_x.append(i+rdm)
        last_y.append(rdm)
    #Returns 2D array, 0=X, 1=Y
    return [last_x, last_y]


#Generates q-size dataset of slices
#Slices taken from j-size data
def datasetBuilder(q, j, dataset=[]):
    for i in range(q):
        up = example_gen(0,j)
        down = example_gen(j,0,-1)
        dataset = getSlices(up, [0,0], dataset)
        dataset = getSlices(down, [1,0], dataset)

    return dataset


#Slices example data
#X1, Y1, X2, Y2
def getSlices(data, label=None, dataset=[]):
    for i in range(0,len(data[0])-N-2, 2):
        build = []
        for j in range(N/2):
            #build = current x,y
            build.append(data[0][i+j])    
            build.append(data[1][i+j])  
        if label:
            dataset.insert(random.randrange(len(dataset)+1), Instance (build, label))
        else:
            dataset.insert(random.randrange(len(dataset)+1), Instance (build))

    return dataset


#Dataset will take the form:
#X + Y values = N-sized timeslice
global N
N = 24

dataset = datasetBuilder(10, 100)

preprocess          = construct_preprocessor( dataset, [standarize] ) 
training_data       = preprocess( dataset )
test_data           = preprocess( dataset )


cost_function       = cross_entropy_cost
settings            = {
    # Required settings
    "n_inputs"              : N,       # Number of network input signals
    "layers"                : [  (20, sigmoid_function), (2, sigmoid_function) ],
                                        # [ (number_of_neurons, activation_function) ]
                                        # The last pair in the list dictate the number of output signals
    
    # Optional settings
    "initial_bias_value"    : 0.0,
    "weights_low"           : -0.1,     # Lower bound on the initial weight value
    "weights_high"          : 0.1,      # Upper bound on the initial weight value
}


# initialize the neural network
network             = NeuralNet( settings )
network.check_gradient( training_data, cost_function )

## load a stored network configuration
# network           = NeuralNet.load_network_from_file( "network0.pkl" )


# Train the network using backpropagation
RMSprop(
        network,                            # the network to train
        training_data,                      # specify the training set
        test_data,                          # specify the test set
        cost_function,                      # specify the cost function to calculate error
        
        ERROR_LIMIT             = 1e-3,     # define an acceptable error limit 
        #max_iterations         = 10000,      # continues until the error limit is reach if this argument is skipped
                                
        batch_size              = 0,        # 1 := no batch learning, 0 := entire trainingset as a batch, anything else := batch size
        print_rate              = 1000,     # print error status every `print_rate` epoch.
        learning_rate           = 0.1,      # learning rate
        momentum_factor         = 0.8,      # momentum
        input_layer_dropout     = 0.0,      # dropout fraction of the input layer
        hidden_layer_dropout    = 0.0,      # dropout fraction in all hidden layers
        save_trained_network    = False     # Whether to write the trained weights to disk
    )


# Print a network test
#print_test( network, training_data, cost_function )


"""
Prediction Example
"""
prediction_vals = example_gen(0,100)
prediction_set = getSlices(prediction_vals)
prediction_set = preprocess( prediction_set )
print " "
print network.predict( prediction_set ) # produce the output signal
