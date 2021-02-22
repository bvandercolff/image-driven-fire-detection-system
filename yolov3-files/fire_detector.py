import subprocess
import os
cmd = './darknet detector test data/obj.data cfg/yolov3_testing.cfg yolov3_training_2.weights data/fire.jpg -thresh 0.02'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

while proc.poll() is None:
    output = proc.stdout.readline() #get line from output
    out = output.decode('UTF-8')    #convert output from type byte to string
    if out.find("fire: ") != -1:
        os.system("python3 sendText.py")
    print(out)
