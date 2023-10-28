# ByLzCv2Camera
Cv2Camera with face detection with using phone

`Information about the latest update is at the very bottom of the Readme`

A short tutorial on using ByLz camera with cv2.

Before you start using it, please read the OpenCV documentation for Python - https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html and https://pypi.org/project/opencv-python/

Also download required haarcascade [https://github.com/opencv/data/haarcascades/haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)


First, install libraries
`pip install -r /path/to/requirements.txt`

We use this 
(https://play.google.com/store/apps/details?id=com.pas.webcam&hl=ru&gl=US&pli=1) 
application for Android as an IP camera, but you can use another

in `main.py`  `url = "http://yourip//shot.jpg"` you will need to insert a link with your IP address. You can get it in the application itself

When everything is ready, you need to launch `menu.py`, we will see the standard greeting
(welcome!
select the operating mode)
![Code_gUTqjpaoDQ](https://github.com/Bytelibz/ByLzCv2Camera/assets/55909716/13acec47-879a-4728-85e5-88cd3bc26de8)

| Mode | Description | Command |
| --- | --- | --- |
| `triggermode` | will send a notification when a face is detected, offer to examine the object | 1 |
| `maincameramode` | will open a permanent view of the window with the camera footage | 2 |

`triggermode`:

You will receive this message - `triggermode started`

When `triggermode()` detects a face, it will prompt you to look at the resulting photo - `Some face detected, do u need to show y/n`

When you write `y`, the last detected face will be shown to you in matplotlib window
![python_cUBMdphkCr](https://github.com/Bytelibz/ByLzCv2Camera/assets/55909716/28427eb6-e7a6-4265-8b28-93bed8ab6e5d)

Also, the last detected face will be saved along the path `data\images`
![explorer_Zrv9Bp3YiP](https://github.com/Bytelibz/ByLzCv2Camera/assets/55909716/0658f4fb-b3d4-493e-95a7-1bcae3f3d143)


If you write `n` then the console will be cleared until the next detection

`maincammode`:

When you run maincammode, a window with a video sequence will immediately open, and all detected faces will be marked on this video sequence
![python_BKLj5RRoEY](https://github.com/Bytelibz/ByLzCv2Camera/assets/55909716/626daf36-100a-4fc5-b20b-524b25872b1e)
To close the window press `esc`



`main.py`:
in `haar_cascade = cv2.CascadeClassifier('C:\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')` 

it is recommended to use the full path to your haar cascade



`cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)` you can change color of rectangle(0, 0, 0) etc.


This is the first version, updates will be released in the future. There are also comments and explanations inside the code

`Updated`:

`Push notifications` are now active in triggermode

![Code_vGXM4HO2a3](https://github.com/Bytelibz/ByLzCv2Camera/assets/55909716/c4d05ecb-0306-4a6b-8fa7-abf69cb525c1)




Now detected face in triggermode  will be displayed using matplotlib and saved in the directory: `data\images`
![python_oY4Tfehp12](https://github.com/Bytelibz/ByLzCv2Camera/assets/55909716/ca1626a1-c489-44ff-b97c-2cf806b20c07)

When you close the matplotlib window, `maincamtrigger()` will continue scanning and again offer to open the photo with the detected face

checkout `requirements.txt` and install matbpotlib via `pip install matplotlib`

checkout `requirements.txt` and install plyer via `pip install plyer`
