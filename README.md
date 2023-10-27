# ByLzCv2Camera
Cv2Camera with face detection with using phone

`Information about the latest update is at the very bottom of the Readme`

A short tutorial on using ByLz camera with cv2.

Before you start using it, please read the OpenCV documentation for Python - https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html and https://pypi.org/project/opencv-python/

First, install libraries
`pip install -r /path/to/requirements.txt`

We use this 
(https://play.google.com/store/apps/details?id=com.pas.webcam&hl=ru&gl=US&pli=1) 
application for Android as an IP camera, but you can use another

When everything is ready, you need to launch `menu.py`, we will see the standard greeting
(welcome!
select the operating mode)
| Mode | Description | Command |
| --- | --- | --- |
| `triggermode` | will send a notification when a face is detected, offer to examine the object | 1 |
| `maincameramode` | will open a permanent view of the window with the camera footage | 2 |

`main.py`:

in `url = "http://yourip//shot.jpg"` you will need to insert a link with your IP address. You can get it in the application itself

`cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)` you can change color of rectangle(0, 0, 0) etc.



This is the first version, updates will be released in the future. There are also comments and explanations inside the code

`Updated`:

Now detected face in triggermode  will be displayed using matplotlib and saved in the directory: `data\images`
![python_oY4Tfehp12](https://github.com/Bytelibz/ByLzCv2Camera/assets/55909716/ca1626a1-c489-44ff-b97c-2cf806b20c07)

