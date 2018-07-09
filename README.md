Contains the codes for an Automated Dispensary system.
The system builds a classifier for images of pills, powered by retraining the final layer of MobileNet architecture.
The classifier directory contains the codes for retraining the classifier and evaluating the image (forked from Google CodeLabs tensorflow-for-poets-2 repo)
It further contains implementations to localize the positions of certain objects in the omage through contour detection and a simple sliding window. (In the Main directory. Most of the IP implementation is in the Testing_contours.py script.)
Further, it has code to commnicate with an Arduino-UNO to recieve orders and control stepper motors.
