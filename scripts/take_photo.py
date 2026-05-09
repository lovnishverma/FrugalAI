import cv2
import os
import sys
import time
from datetime import datetime


def snap_photo():
    # Folder to save the images
    path = r"C:\Users\princ\Pictures\Camera_Snaps"

    try:
        if not os.path.exists(path):
            os.makedirs(path)

        filename = f"photo_{datetime.now().strftime('%H%M%S')}.jpg"
        fullpath = os.path.join(path, filename)

        # 0 is usually the default built-in webcam.
        # CAP_DSHOW is required for Windows background scripts to load instantly.
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        if not cap.isOpened():
            print("Error: Could not access the webcam. Is it in use by another app?")
            return

        # Warm-up time for sensor to adjust light/focus
        time.sleep(1.5)

        # Read the frame
        ret, frame = cap.read()

        if ret:
            cv2.imwrite(fullpath, frame)
            print(f"Photo snapped and saved: {fullpath}")
        else:
            print("Error: Camera opened but failed to capture the image.")

    except Exception as e:
        print(f"Camera Script Error: {e}")
    finally:
        # ALWAYS release the camera, otherwise the LED stays on and it's locked out
        if 'cap' in locals() and cap.isOpened():
            cap.release()


if __name__ == "__main__":
    snap_photo()
    sys.stdout.flush()  # Push the log to OpenClaw
    sys.exit(0)         # Kill the background thread instantly
