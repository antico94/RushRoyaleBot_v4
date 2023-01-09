from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

# Load the model
model = load_model('units_model.h5')
img_width, img_height = 55, 57

# Define the data generators for test data
test_datagen = ImageDataGenerator(rescale=1./255)

test_dir = 'C:/Users/Meiu/Desktop/unit'

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=20,
    class_mode='categorical')

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_generator, verbose=1)
print('Test accuracy:', test_acc)