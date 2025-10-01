
import math


def relu(x):

    return max(0, x)


def sigmoid(x):

    return 1 / (1 + math.exp(-x))


def multi_layer_perceptron(inputs):

    # Weights and biases for the first hidden layer (2 nodes to 3 nodes)
    weights_hidden1 = [
        [0.2, 0.3],  
        [0.5, 0.4],  
        [0.6, 0.7]   
    ]
    biases_1 = [0.1, 0.2, 0.3]  

    # Weights and biases for the second hidden layer (3 nodes to 2 nodes)
    weights_hidden2 = [
        [0.4, 0.3, 0.5],
        [0.7, 0.6, 0.2]  
    ]
    biases_2 = [0.2, 0.1]

    # Weights and biases for the third hidden layer (2 nodes to 2 nodes)
    weights_hidden3 = [
        [0.6, 0.5],  
        [0.3, 0.4]   
    ]
    biases_3 = [0.3, 0.2] 
    # Weights and biases for the output layer (2 nodes to 1 node)
    weights_output = [0.7, 0.8]
    bias_output = 0.1

    # first hidden layer outputs
    hidden1 = []
    for i in range(3):
        node_input = sum(inputs[j]*weights_hidden1[i][j] for j in range(2))
        node_input += biases_1[i]
        hidden1.append(relu(node_input))

    # second hidden layer outputs
    hidden2 = []
    for i in range(2):
        node_input = sum(hidden1[j]*weights_hidden2[i][j] for j in range(3))
        node_input += biases_2[i]
        hidden2.append(relu(node_input))

    # third hidden layer outputs
    hidden3 = []
    for i in range(2):
        node_input = sum(hidden2[j]*weights_hidden3[i][j] for j in range(2))
        node_input += biases_3[i]
        hidden3.append(relu(node_input))

    # output layer
    output = sum(hidden3[i]*weights_output[i] for i in range(2))
    output += bias_output
    return sigmoid(output)

# user input
print("Disease Diagnosis Neural Network")
blood_pressure = float(input("Enter blood pressure level (e.g. 120): "))
heart_rate = float(input("Enter heart rate (e.g. 80): "))


inputs = [blood_pressure, heart_rate]
result = multi_layer_perceptron(inputs)


print(f"\nPredicted Disease Risk Level: {result:.4f} (0 = Low, 1 = High)")
