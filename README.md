# About this package
* **Author** : Natanan Tirasukvongsa (Mai)
* **Package** : mai
* **Detail** : Ubuntu 20.04 Lts, ROS2 (Foxy)
* **Place** : Thavida Lab (Humanoid Soccer RoboCup), KMUTT, Thailand
* **Contact** : tnatanan@gmail.com

# Document
* **File** : [รายงานความคืบหน้า_ณัฐนันท์.pdf](https://github.com/Natanan-Tirasukvongsa/mai/files/11497313/_.pdf)

# Installation
1. Install ROS2 Foxy by following this [tutorial](https://docs.ros.org/en/foxy/Installation.html)
2. Open terminal (Ctrl+Alt+t)
3. Install Colcon and create workspace by following this [tutorial](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html)
```
sudo apt install python3-colcon-common-extensions
mkdir -p ~/ros2_ws/src
```
4. Clone mai package
```
cd ~/ros2_ws/src
git clone https://github.com/Natanan-Tirasukvongsa/mai.git 
```
5. Build the workspace with colcon
```
cd ..
colcon build --packages-select mai
```
6. Source the setup file
```
source install/local_setup.bash
```

# Launch File
## Launch URDF file
1. Open New terminal
2. Launch command line 
```
ros2 launch mai display.launch.py
```

| ![Screenshot from 2023-05-17 18-29-40](https://github.com/Natanan-Tirasukvongsa/mai/assets/78638430/951df0da-461f-4135-9c1b-5da69374ba81) | 
|  :---: | 
| URDF - Cylinder  | 

## Launch trajectory and display axis 
1. Open New terminal
2. Launch command line  
```
ros2 launch mai test_display.launch.py 
```
|![Screenshot from 2023-05-17 18-32-49](https://github.com/Natanan-Tirasukvongsa/mai/assets/78638430/d3b1557d-4e8d-4ce4-9a72-e6d7f9f3925c) | 
|  :---: | 
| Axis moves by following trajectory  | 

## Launch only trajectory
1. Open New terminal
2. Launch command line  
```
ros2 launch mai test_traj_launch.py 
```
|![Screenshot from 2023-05-17 18-39-39](https://github.com/Natanan-Tirasukvongsa/mai/assets/78638430/ac6c72d1-4a30-4bb6-840f-8d2801c0782d)| 
|  :---: | 
| Trajectory  | 

# Service and Action File
## Server and Client Trajectory
1. copy config_inv.yaml path (**Name** is your computer name)

```
/home/Name/ros2_ws/src/mai/config/config_inv.yaml
```

2. Change yaml file directory in humanoid_inv.py (line 6)
- humanoid_inv.py is in /home/**Name**/ros2_ws/src/mai/mai/humanoid_inv.py 
- Open this file 
```
cd ~/ros2_ws/src/mai/mai
gedit humanoid_inv.py
```
- Edit line 6 (paste new directory)
```
with open('/home/Name/ros2_ws/src/mai/config/config_inv.yaml', 'r') as file:
```
- Save file

3. **Please Check : Python executables**
- Open CMakeLists.txt
```
cd ~/ros2_ws/src/mai
gedit CMakeLists.txt
```
- Add other Python executables (if you have never had yet) 
```
# Install Python executables
install(PROGRAMS 
  mai/ser_fw_xyz_parent.py
  mai/humanoid_foot_traj_inherit_ser.py 
) 
```
> if there are following python executables, you can skip

4. **Please Check : Import file name** 
- open ser_fw_xyz_parent.py 
```
cd ~/ros2_ws/src/mai/mai
gedit ser_fw_xyz_parent.py 
```
- Change **humanoid_foot_traj** to **humanoid_foot_traj_inherit_ser** (line 10)
> if import file name is correct, you can skip

5. Build the workspace with colcon
```
cd ~/ros2_ws
colcon build --packages-select mai
```
6. Source the setup file
```
source install/local_setup.bash
```
7. Run service node
```
ros2 run mai ser_fw_xyz_parent.py 
```
8. Open another terminal and run client node
```
ros2 run mai cli_inv_th.py 
```
