
'''
Instructions:
Point webcam at a preferably white background.
Results may vary depending on lighting conditions, Camera, etc.
If far from Camera: Insert fingers in to the Region of Interest (ROI).
If close to Camera: Insert hand into ROI.
There may be minor lag when the hand enters the ROI.

Fist or 1 finger: Spacebar (Pause, unpause on Youtube).
2 fingers: Volume up on Windows. Insert fingers into ROI simultaneously. Do not stagger.
3 fingers: Volume down on Windows. Insert fingers into ROI simultaneously. Do not stagger.
4 fingers: Volume mute on Windows. Unmute with volume up or down. Insert fingers into ROI simultaneously. Do not stagger

Press Q while Python window is in foreground to stop the program.
Note: [Warn:0] is thrown on termination. It seems this particular warning is due to Environment Variables in Windows.

'''

import cv2
import pyautogui


# Because I think "Null" instead of pass for some reason.
def null():
    pass


hand_cascade = cv2.CascadeClassifier('hand.xml')
capture = cv2.VideoCapture(0)
# Colors are in BGR
#      B  G   R
red = (0, 0, 255)
teal = (128, 128, 0)
skin_lower = [0, 48, 80]
skin_upper = [20, 255, 255]
upper_left = (300, 100)
lower_right = (500, 300)

while True:

    # misc capture stuff + frame variables
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)

    roi = frame[100:300, 300:500]
    cv2.rectangle(frame, upper_left, lower_right, red, 5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # setting variable and params for detection
    hands = hand_cascade.detectMultiScale(roi, 1.05, minNeighbors=25)
    hand_len = len(hands)

    # create a rectangle around hand or fingers
    for (x, y, w, h) in hands:
        cv2.rectangle(roi, (x, y), (x + w, y + h), teal, 3)

    # activation station. Uses length of hands variable to trigger pyautogui functions.
    if hand_len == 1:
        pyautogui.press("space", interval=2)
        print("spacebar")

    if hand_len == 2:
        pyautogui.press("volumeup")
        print("Volume Up")

    if hand_len == 3:
        pyautogui.press("volumedown")
        print("Volume Down")

    if hand_len == 4:
        pyautogui.press("volumemute", interval=2)
        print("Mute Sound")

    if hand_len >= 5:
        null()

    cv2.imshow("frame", frame)

    # Q key is exit if python window is in foreground
    wk = cv2.waitKey(0) & 0xFF
    if wk == ord('q'):
        print("Q PRESSED - CLOSING.")
        capture.release()
        cv2.destroyAllWindows()
        break

capture.release()
cv2.destroyAllWindows()
