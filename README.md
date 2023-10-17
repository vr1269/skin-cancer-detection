![image](https://github.com/MainakRepositor/Carcinoskin/assets/64016811/8f5a1cdc-2397-44f5-8b81-a153f9780e0e)


# Carcinoskin
This project uses deep learning algorithms and the Keras library to determine if a person has certain diseases or not from their chest x-rays and other scans. The trained model is displayed using Streamlit, which enables the user to upload an image and receive instant feedback.

Essentially it uses 6 different CNN models to diagnose 6 different diseases :- Covid, Glaucoma, Skin Cancer, Pneumonia, Tuberculosis and Brain Tumor classification
Covid and Pnemonia are detected using chest X-ray scans of the patient while Gluacoma uses an internal scan of the eye and Skin Cancer is detected
using external pictures

## Our Model
Below is the summary of our CNN model which we have made using python and keras.

### Model for Covid & Pneumonia Classification

| Layer (type)                  | Output Shape             | Param #     |
|-------------------------------|--------------------------|-------------|
| conv2d (Conv2D)               | (None, 222, 222, 32)     | 896         |
| max_pooling2d (MaxPooling2D)  | (None, 111, 111, 32)     | 0           |
| conv2d_1 (Conv2D)             | (None, 109, 109, 64)     | 18496       |
| max_pooling2d_1 (MaxPooling2D)| (None, 54, 54, 64)       | 0           |
| conv2d_2 (Conv2D)             | (None, 52, 52, 128)      | 73856       |
| max_pooling2d_2 (MaxPooling2D)| (None, 26, 26, 128)      | 0           |
| flatten (Flatten)             | (None, 86528)            | 0           |
| dense (Dense)                 | (None, 128)              | 11075712    |

As you can see this is a simple Neural Network with 8 layers. (this had an accuracy of approx 0.93 on average)
Each Layer has a specific job in order to get the desired output, they are :-

- Convolutional layer (conv2d): This layer takes an input image and applies a set of 32 filters to produce 32 output feature maps. Each filter extracts a particular feature from the image. The output of this layer has a shape of (None, 222, 222, 32).

- Max pooling layer (max_pooling2d): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 111, 111, 32).

- Convolutional layer (conv2d_1): This layer applies a set of 64 filters to the output of the previous layer to produce 64 output feature maps. The output of this layer has a shape of (None, 109, 109, 64).

- Max pooling layer (max_pooling2d_1): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 54, 54, 64).

- Convolutional layer (conv2d_2): This layer applies a set of 128 filters to the output of the previous layer to produce 128 output feature maps. The output of this layer has a shape of (None, 52, 52, 128).

- Max pooling layer (max_pooling2d_2): This layer reduces the dimensionality of the output of the previous layer by taking the maximum value in each 2x2 region. The output of this layer has a shape of (None, 26, 26, 128).

 - Flatten layer (flatten): This layer flattens the output of the previous layer into a 1D vector. The output of this layer has a shape of (None, 86528).

- Fully connected layer (dense): This layer takes the flattened vector from the previous layer and applies 128 neurons to it, producing a 128-dimensional output. The output of this layer has a shape of (None, 128).



### Skin Cancer
#### Positive (Malignant)
 ![90](https://user-images.githubusercontent.com/77538244/234957957-e0c19cbe-9988-45c8-9d4f-84382ea40014.jpg)

