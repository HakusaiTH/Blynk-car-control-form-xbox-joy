import cv2

# URL for the video stream
url = 'http://192.168.2.150/videostream.cgi?user=admin&pwd=123456789'

# Open the video stream
cap = cv2.VideoCapture(url)

# Check if the video stream was successfully opened
if not cap.isOpened():
    print("Error: Could not open video stream.")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("Failed to retrieve frame.")
            break

        # Display the frame
        cv2.imshow('Video Stream', frame)

        # Press 'q' to exit the video stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close display window
cap.release()
cv2.destroyAllWindows()
