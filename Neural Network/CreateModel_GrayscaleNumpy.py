import os

import numpy as np
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from tqdm import tqdm

# Load the data
data_dir = 'C:/Users/Meiu/Desktop/short_unit_np'
x_train = []
y_train = []
total_files = 0
for subdir in os.listdir(data_dir):
    subdir_path = os.path.join(data_dir, subdir)
    if os.path.isdir(subdir_path):
        total_files += len([f for f in os.listdir(subdir_path) if f.endswith('.npy')])

with tqdm(total=total_files, unit='file') as pbar:
    for subdir in os.listdir(data_dir):
        subdir_path = os.path.join(data_dir, subdir)
        if os.path.isdir(subdir_path):
            for image_file in os.listdir(subdir_path):
                if image_file.endswith('.npy'):
                    image_path = os.path.join(subdir_path, image_file)
                    image = np.load(image_path)
                    image = np.dot(image[...,:3], [0.2989, 0.5870, 0.1140]) # Convert to grayscale
                    x_train.append(image)
                    y_train.append(subdir)
                    pbar.update()

x_train = np.array(x_train)
y_train = np.array(y_train)

# Preprocess the labels
label_encoder = LabelEncoder()
y_train = label_encoder.fit_transform(y_train)
y_train = to_categorical(y_train)

# Create the model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(57, 57, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(8, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10)
model.save('GeneratedModels/units_model_np_grayscale.h5')