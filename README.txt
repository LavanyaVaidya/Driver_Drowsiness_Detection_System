Driver Drowsiness detection 

Dataset : https://www.kaggle.com/datasets/lavanyavaidya/ourdatasetddd/versions/1

Use latest version (version2) to train VGG16/VGG19
Use older version (version1) to train model3

Launcher file is used to present a GUI where we can choose the model of our choice to start the drowsiness detection. 

Kaggle_both is using model 3 and detecting both eyes and mouth.
Kaggle_eyes is using model 3 and detecting only eyes.
Kaggle_mouth is using model 3 and detecting only mouth.

VGG16_both is using model VGG16 and detecting both eyes and mouth.
VGG16_eyes is using model VGG16 and detecting only eyes.
VGG16_mouth is using model VGG16 and detecting only mouth.

VGG19_both is using model VGG19 and detecting both eyes and mouth.
VGG19_eyes is using model VGG19 and detecting only eyes.
VGG19_mouth is using model VGG19 and detecting only mouth.

Choose any of the above option using launcher_file to start the detection.
After detection, close the camera feed by pressing 'q'.