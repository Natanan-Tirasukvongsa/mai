# About this package
* Author : Natanan Tirasukvongsa (Mai)
* Package : mai
* Detail : Ubuntu 20.04 Lts, ROS2 (Foxy)
* Place : Thavida Lab (Humanoid Soccer RoboCup), KMUTT, Thailand
* Contact : tnatanan@gmail.com

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
## Launch trajectory and display axis 
1. Open New terminal
2. Launch command line  
```
ros2 launch mai test_display.launch.py 
```
## Launch only trajectory
1. Open New terminal
2. Launch command line  
```
ros2 launch mai test_traj_launch.py 
```

# Service and Action File
## Server and Client Trajectory
1. copy config_inv.yaml path

```
/home/Name/ros2_ws/src/mai/config/config_inv.yaml
```

- Name is your computer name

2. Change yaml file directory in humanoid_inv.py (line 6)

```
with open('/home/Name/ros2_ws/src/mai/config/config_inv.yaml', 'r') as file:
```

3. **Please Check : Python executables**
- Add Python executables (if you have never had yet) <br />
install(PROGRAMS <br />
  ... <br />
  **mai/ser_fw_xyz_parent.py** <br />
  **mai/humanoid_foot_traj_inherit_ser.py** <br />
  ... <br />
) <br />
- if there are following python executables, you pass this process

4. **Please Check : import file name** 
- open ser_fw_xyz_parent.py 
- Change **humanoid_foot_traj** to **humanoid_foot_traj_inherit_ser** (line 10)
- if import file name is correct, you pass this process
5. run service node
```
ros2 run mai ser_fw_xyz_parent.py 
```
6. run client node
```
ros2 run mai cli_inv_th.py 
```
