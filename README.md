# ByLzCv2Camera
Cv2Camera with face detection with using phone

A short tutorial on using ByLz camera with cv2.

Before you start using it, please read the OpenCV documentation for Python - https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html and https://pypi.org/project/opencv-python/

First, install libraries
`pip install -r /path/to/requirements.txt`

We use this 
(https://play.google.com/store/apps/details?id=com.pas.webcam&hl=ru&gl=US&pli=1) 
application for Android as an IP camera, but you can use another

When everything is ready, you need to launch menu.py, we will see the standard greeting
(welcome!
select the operating mode)
| Mode | Description |
| --- | --- |
| `triggermode` | will send a notification when a face is detected, offer to examine the object |
| `maincameramode` | will open a permanent view of the window with the camera footage |

`main.py`:

in `url = "http://yourip//shot.jpg"` you will need to insert a link with your IP address. You can get it in the application itself

`cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)` you can change color of rectangle(0, 0, 0) etc.



This is the first version, updates will be released in the future. There are also comments and explanations inside the code
