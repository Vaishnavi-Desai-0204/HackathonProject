import tensorflow as tf
import numpy as np
import os
import random
import cv2

# Load the wardrobe data
wardrobe = np.load('wardrobe.npy', allow_pickle=True)

# Split the data into training and validation sets
random.shuffle(wardrobe)
train_split = int(len(wardrobe) * 0.8)
train_data = wardrobe[:train_split]
val_data = wardrobe[train_split:]

# Define a function to preprocess the images
def preprocess_image(image):
    # Resize the image to (224, 224) if necessary
    if image.shape[:2] != (224, 224):
        image = cv2.resize(image, (224, 224))
    # Convert the image from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Normalize the pixel values to be between 0 and 1
    image = image / 255.0
    return image

# Preprocess the training and validation data
train_images = np.array([preprocess_image(img) for img in train_data[:, 0]])
train_labels = train_data[:, 1].astype(np.float32)
val_images = np.array([preprocess_image(img) for img in val_data[:, 0]])
val_labels = val_data[:, 1].astype(np.float32)

# Define the model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(
    x=train_images,
    y=train_labels,
    batch_size=32,
    epochs=10,
    validation_data=(val_images, val_labels)
)

# Save the trained model
model.save('polyvore_cnn.h5')
