# import tensorflow as tf
# from tensorflow.keras import layers, models, regularizers

# def build_cnn_model(input_shape=(128, 128, 3), num_classes=5):
#     model = models.Sequential([
#         # Conv Block 1
#         layers.Conv2D(32, (3,3), activation="relu", padding="same", input_shape=input_shape),
#         layers.BatchNormalization(),
#         layers.MaxPooling2D((2,2)),

#         # Conv Block 2
#         layers.Conv2D(64, (3,3), activation="relu", padding="same"),
#         layers.BatchNormalization(),
#         layers.MaxPooling2D((2,2)),

#         # Conv Block 3
#         layers.Conv2D(128, (3,3), activation="relu", padding="same"),
#         layers.BatchNormalization(),
#         layers.MaxPooling2D((2,2)),
#         layers.Dropout(0.3),

#         # Conv Block 4 (extra for better features)
#         layers.Conv2D(256, (3,3), activation="relu", padding="same"),
#         layers.BatchNormalization(),
#         layers.MaxPooling2D((2,2)),
#         layers.Dropout(0.3),

#         # Fully Connected Layers
#         layers.Flatten(),
#         layers.Dense(256, activation="relu", kernel_regularizer=regularizers.l2(0.001)),
#         layers.BatchNormalization(),
#         layers.Dropout(0.5),

#         # Output Layer
#         layers.Dense(num_classes, activation="softmax")
#     ])

#     model.compile(
#         optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
#         loss="sparse_categorical_crossentropy",
#         metrics=["accuracy"]
#     )
#     return model










import tensorflow as tf
from tensorflow.keras import layers, models

def build_cnn_model(input_shape=(128, 128, 3), num_classes=5):
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation="relu", input_shape=input_shape),
        layers.MaxPooling2D((2,2)),

        layers.Conv2D(64, (3,3), activation="relu"),
        layers.MaxPooling2D((2,2)),

        layers.Conv2D(128, (3,3), activation="relu"),
        layers.MaxPooling2D((2,2)),

        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax")
    ])
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model