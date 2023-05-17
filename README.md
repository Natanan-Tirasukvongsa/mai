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

