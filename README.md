# **Kalman Filter Overview**

## **Why are Kalman Filters Useful?**
Kalman filters excel at processing noisy sensor data to provide more accurate estimates and predictions. This makes them particularly valuable in applications like autonomous vehicle systems, where they can be used for object tracking.  
*(Source: Udacity, Intro to Self-Driving Cars)*

## **Kalman Filters and Sensors**
In object tracking for autonomous vehicles, radar and lidar sensors are commonly used. Radar sensors can directly measure both the distance and velocity of objects. In contrast, lidar sensors only measure distance.  

To understand how a Kalman filter can improve tracking, consider using lidar data alone. Suppose a bicyclist is riding in front of your vehicle. A lidar signal is sent out and returns, indicating that the bicycle is 10 meters ahead. However, lidar does not provide any information about the bicycle’s velocity.

After 0.05 seconds, the lidar sends another signal. This time, it shows the bicycle is 9.95 meters away. Now, you can estimate that the bicycle is moving towards you at -1 meter per second. Although your vehicle can predict the bicycle’s position between signals, it doesn’t have complete velocity data until after each new lidar measurement.  
*(Source: Udacity, Intro to Self-Driving Cars)*

## **Dealing with Sensor Noise**
Unfortunately, both lidar and radar signals are prone to noise, meaning their measurements can be somewhat inaccurate. This is where Kalman filters prove to be incredibly useful. A Kalman filter helps to "smooth out" this noisy data, allowing for more precise estimates of an object's true position and velocity.

The Kalman filter operates by balancing two sources of uncertainty:
- **Your prediction’s uncertainty**: How confident you are in your model’s estimate of the object’s position.
- **Sensor measurement uncertainty**: How reliable the sensor data is, given the noise.

If your prediction has high uncertainty, the Kalman filter assigns more weight to the sensor’s data. Conversely, if the sensor data is noisy, the filter gives more weight to your predicted position.

## **Technologies Used**
- **Python**
- **Object-Oriented Design**
- **Jupyter Notebook**
- **Data Visualization**
- **Machine Learning**
- **Artificial Intelligence (AI)**
- **Localization and Prediction**
- **Data Structures**

![alt](https://github.com/jackyhuynh/kalmanFilter-app/blob/main/src/picture/1.PNG)
