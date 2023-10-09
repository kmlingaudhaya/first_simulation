# first_simulation

In this project I have modelled a simple robot eith a cuboid and 4 cylinders and simulated it in gazebo using a python script to teleoperate the bot by publishing twist msgs to the cmd_vel topic.

Let's go step by on the process.

First, we define a workspace for our work purpose and then we create a package inside it using ROS commands.

```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
The catkin_make command is a convenience tool for working with catkin workspaces. Running it the first time in your workspace, it will create a CMakeLists.txt link in your 'src' folder. 

Now once we have created a workspace, we go on create a package in the workspace to work with.

```bash
$ cd ~/catkin_ws/src
```
we navigate inside the source folder and create a package there
```bash
$ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
```
here the std_msgs rospy and roscpp are the dependencies of the package

```bash
workspace_folder/        -- WORKSPACE
  src/                   -- SOURCE SPACE
    CMakeLists.txt       -- 'Toplevel' CMake file, provided by catkin
    package_1/
      CMakeLists.txt     -- CMakeLists.txt file for package_1
      package.xml        -- Package manifest for package_1
    ...
    package_n/
      CMakeLists.txt     -- CMakeLists.txt file for package_n
      package.xml        -- Package manifest for package_n
```

After creating the package successfully, we source the workspace everytime we build it.
<br>
This is basically done for ease of running multiple packages with different dependencies and so on.

Workflow Flexibility: Sourcing the setup.bash script gives you flexibility. You can have multiple workspaces, each with its own set of packages and dependencies, and you can choose which workspace to use by sourcing the corresponding devel/setup.bash script


once this basic setup is over, we procede to open multiple folders inside the package beginner tutorials in 

catkin_ws/src/beginner_tutorials

The folders are as follows

beginner_tutorials

                    1)gazebo
                    
                    2)launch
                    
                    3)scripts
                    
                    4)urdf


In urdf folder we create a .urdf.xacro file to describe the bot.

In scripts we write the key_reader scripts required to teleoperate the bot.

Launch file is used to launch the urdf bot in Rviz to visualize and also used to launch the bot in gazebo to check for physics compatibility.

In gazebo folder we add the plugins required to operate the bot. It can be skid steering or differential drive
<br>
the plugins are imported from the folloeing link
<br>
      
      https://classic.gazebosim.org/tutorials?tut=ros_gzplugins



https://github.com/kmlingaudhaya/first_simulation/issues/1#issue-1932812580


