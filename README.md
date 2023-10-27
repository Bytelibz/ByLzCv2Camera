# ByLzCv2Camera
Cv2Camera with face detection with using phone

A short tutorial on using ByLz camera with cv2.

First, install libraries
`pip install -r /path/to/requirements.txt`

We use this 
(https://play.google.com/store/apps/details?id=com.pas.webcam&hl=ru&gl=US&pli=1) 
application for Android as an IP camera

When everything is ready, you need to launch menu.py, we will see the standard greeting
(welcome!
select the operating mode)
| Mode | Description |
| --- | --- |
| `triggermode` | will send a notification when a face is detected, offer to examine the object |
| `maincameramode` | will open a permanent view of the window with the camera footage |
This is the first version, updates will be released in the future. There are also comments and explanations inside the code
