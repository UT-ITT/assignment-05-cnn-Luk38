import cv2
import numpy as np
from keras.models import load_model
from pynput.keyboard import Controller, Key
import time

# include only those gestures
CONDITIONS = ['like', 'no_gesture', 'stop', 'dislike', 'two_up']

# image size
IMG_SIZE = 64
SIZE = (IMG_SIZE, IMG_SIZE)

# number of color channels we want to use
# set to 1 to convert to grayscale
# set to 3 to use color images
COLOR_CHANNELS = 3

# load the trained model
model = load_model("03-media_control/gesture_recognition_vgg.keras")

keyboard = Controller()

# helper function to pre-process images (color channel conversion and resizing)
def preprocess_image(img):
    if COLOR_CHANNELS == 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_resized = cv2.resize(img, SIZE)
    img_resized = img_resized.astype('float32') / 255.0

    return img_resized

# open the webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError('Could not open the webcam')

# Cooldown 
last_action_time = 0
COOLDOWN = 1.5  

#camera loop
while True:
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError('Could not read a frame from the webcam')
    
    frame = cv2.flip(frame, 1)  # flip the frame horizontally (mirror image)

    # region of interest (ROI) for gesture detection
    x1, y1 = 150, 100
    x2, y2 = 450, 400

    roi = frame[y1:y2, x1:x2]

    cv2.rectangle(frame, (x1, y1), (x2, y2),
                  (0, 255, 0), 2)

    img = preprocess_image(roi)
    img = np.expand_dims(img, axis=0)

    # predict the gesture
    prediction = model.predict(img, verbose=0)

    condition_index = np.argmax(prediction)

    condition = CONDITIONS[condition_index]
    confidence = np.max(prediction)

    cv2.putText(
        frame,
        f"{condition} ({confidence:.2f})",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    # check gestures when confidence is above threshold and cooldown has passed
    current_time = time.time()
    if confidence > 0.8 and current_time - last_action_time >= COOLDOWN:
        if condition == 'like':
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            print("Volume Up")
        elif condition == 'stop':
            keyboard.press(Key.media_play_pause)
            keyboard.release(Key.media_play_pause)
            print("Play/Pause")
        elif condition == 'dislike':
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            print("Volume Down")
        elif condition == 'two_up':
            keyboard.press(Key.media_next)
            keyboard.release(Key.media_next)
            print("Next Track")
        elif condition == 'no_gesture':
            print("No Gesture Detected")

        last_action_time = current_time

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # Close the Window with Q
        break
    
cap.release()
cv2.destroyAllWindows()
