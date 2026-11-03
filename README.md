# IOER – Introduction to Object and Event Recognition

Laboratory exercises for the course *Introduction to Object and Event Recognition* at Poznan University of Technology. The exercises cover classical computer vision with OpenCV in Python: edge detection, local feature matching and background modeling in video.

## Repository Structure

* [`LAB1`](LAB1/) – **Edge detection.** Gradient operators (Sobel, Prewitt, Scharr) applied to a test image, with Gaussian pre-smoothing, different kernel sizes and thresholds, and a live webcam test. The report compares the operators and discusses how kernel size, threshold and blur affect noise and detail. Includes the report [`lab1_Budimir.pdf`](LAB1/lab1_Budimir.pdf).
  
* [`LAB2/`](LAB2/) – **SIFT (Scale-Invariant Feature Transform).** Detecting keypoints, analyzing the 128-element descriptor and keypoint attributes (angle, octave, scale), tuning SIFT parameters, real-time keypoints from a webcam, feature matching with Lowe's ratio test, and building a panorama with a homography. Solved in the notebook [`Budimir_lab2.ipynb`](LAB2/Budimir_lab2.ipynb), with the standalone scripts [`6.py`](LAB2/6.py) (live webcam) and [`7.py`](LAB2/7.py) (matching).
  
* [`LAB3/`](LAB3/) – **Background modeling.** Estimating the background from a highway video with the mean and the median of 101 frames, generating a foreground mask with [`absdiff`](LAB3/absdiff) and a threshold, and comparing the MOG2 and KNN background subtractors with different parameters. The task is a background subtractor with a selectable mean or median model [(`task.py`)](LAB3/task.py). MOG2 with [`varThreshold=50`](LAB3/varThreshold=50) gave the cleanest mask in my experiments, and the median model gave a much cleaner mask than the mean. Includes the instructions and the report [`Background__modeling_lab_Budimir.pdf`](LAB3/Background__modeling_lab_Budimir.pdf).

## Technologies

Python, OpenCV, NumPy, Matplotlib, Jupyter Notebook

## Running the Code

```bash
pip install opencv-python numpy matplotlib
```

Run each script from inside its own lab folder, because the images and the video are loaded with relative paths. The live webcam examples (`LAB1`, `LAB2/6.py`) need a connected camera, and SIFT requires OpenCV 4.4 or newer.

## Author

Karla Budimir
Poznan University of Technology
