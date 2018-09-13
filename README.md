# Smartbell - The Smart Dumbell
Odometry features from on-board sensors are streamed into an artificial neural network, providing real-time haptic feedback for the user to help minimise their risk of injury whilst exercising and generate useful heuristics on the workout.

This repository contains all the code housed on-board the Smartbell:

# Pi
Code for interacting with the hardware sensors and haptic feedback soldered to the Raspberry Pi.

# Belle:
Neural network implementation. Interprets the data stream from the sensors and outputs appropriate feedback.

# mothership:
Code to provide data to an online server, which in turn will relay it to the user's phone app.

