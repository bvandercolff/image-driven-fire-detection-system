This file gives a step by step install process for the entire darknet/yolov3 system.

Installing darknet:

-Assuming you have set up raspberry pi, updated, and expanded file system

1. Install CMake:

sudo apt-get install build-essential cmake unzip pkg-config


2. Install image and video libraries:

sudo apt-get install libjpeg-dev libpng-dev libtiff-dev  
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev  
sudo apt-get install libxvidcore-dev libx264-dev  


3. Install GTK, GUI backend [May not be necessary, I need to test]

sudo apt-get install libfontconfig1-dev libcairo2-dev  
sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev  
sudo apt-get install libgtk2.0-dev libgtk-3-dev  


4. Install two packages containing numerical optimizations for OpenCV:

sudo apt-get install libatlas-base-dev gfortran  
sudo apt-get install python3-dev  
sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103  
sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5  


5. Install Python 3 

sudo apt-get install python3-dev  


6. Install virtualenv and virtualenvwrapper to enable virtual environments for python development

wget https://bootstrap.pypa.io/get-pip.py  
sudo python get-pip.py  
sudo python3 get-pip.py  
sudo rm -rf ~/.cache/pip  
sudo pip install virtualenv virtualenvwrapper  


7. Add lines to ~/.bashrc

echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc  
echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc  
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc  
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc  


8. Source ~/.bashrc:

source ~/.bashrc  


9. Create virtual environment to hold opencv 4 and additional packages

mkvirtualenv cv -p python3  


10. Install PiCamera API:

pip install "picamera[array]"  


11. Intall OpenCV

pip install opencv-contrib-python==4.1.0.25  


12. Download AlexeyAB darknet fork

git clone https://github.com/AlexeyAB/darknet  


13. Navigate to /home/pi/darknet


14. Edit Makefile, change GPU=0, CUDNN=0, AVX=0, CUDNN_HALF=0, OPENCV=1, LIBSO=0, ZED_CAMERA=0, ZED_CAMERA_v2_8=0


15. Navigate to darknet and compile

cd ~/darknet  
make  


Now darknet should be working, type './darknet' while in the darknet directory to test 


16. Download model files and place each file into the following directories:

yolov3 files:

yolov3_testing.cfg ---> darknet/cfg  
yolov3_training_2.weights ---> darknet  
obj.data --> darknet/data  
obj.names --> darknet/data  
images.zip --> extract to: --> darknet/data/obj  
train.txt --> darknet/data  
 
Now, to test on an image, put the image in darknet/data and enter the following command:

./darknet detector test data/obj.data cfg/yolov3_testing.cfg yolov3_training_2.weights data/(file name)
