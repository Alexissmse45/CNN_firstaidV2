from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
from model.cnn_model import build_cnn_model

# Parameters
IMG_SIZE = (128,128)
BATCH_SIZE = 16
EPOCHS = 10
DATASET_PATH = "datasets"

# Data generator with augmentation
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

train_gen = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='sparse',
    subset='training'
)

val_gen = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='sparse',
    subset='validation'
)

# Build model
num_classes = len(train_gen.class_indices)
model = build_cnn_model(input_shape=(IMG_SIZE[0], IMG_SIZE[1],3), num_classes=num_classes)

# Train
history = model.fit(
    train_gen,
    validation_data=val_gen,
    epochs=EPOCHS
)

# Save model
model.save("first_aid_cnn_model.h5")
