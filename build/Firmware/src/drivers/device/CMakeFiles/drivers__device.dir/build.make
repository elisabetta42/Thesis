# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sdu/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sdu/catkin_ws/build

# Include any dependencies generated for this target.
include Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/depend.make

# Include the progress variables for this target.
include Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/progress.make

# Include the compile flags for this target's objects.
include Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/flags.make

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/flags.make
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o: /home/sdu/catkin_ws/src/Firmware/src/drivers/device/CDev.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sdu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__device.dir/CDev.cpp.o -c /home/sdu/catkin_ws/src/Firmware/src/drivers/device/CDev.cpp

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__device.dir/CDev.cpp.i"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sdu/catkin_ws/src/Firmware/src/drivers/device/CDev.cpp > CMakeFiles/drivers__device.dir/CDev.cpp.i

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__device.dir/CDev.cpp.s"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sdu/catkin_ws/src/Firmware/src/drivers/device/CDev.cpp -o CMakeFiles/drivers__device.dir/CDev.cpp.s

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o.requires:

.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o.requires

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o.provides: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o.requires
	$(MAKE) -f Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build.make Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o.provides.build
.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o.provides

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o.provides.build: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o


Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/flags.make
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o: /home/sdu/catkin_ws/src/Firmware/src/drivers/device/ringbuffer.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sdu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__device.dir/ringbuffer.cpp.o -c /home/sdu/catkin_ws/src/Firmware/src/drivers/device/ringbuffer.cpp

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__device.dir/ringbuffer.cpp.i"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sdu/catkin_ws/src/Firmware/src/drivers/device/ringbuffer.cpp > CMakeFiles/drivers__device.dir/ringbuffer.cpp.i

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__device.dir/ringbuffer.cpp.s"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sdu/catkin_ws/src/Firmware/src/drivers/device/ringbuffer.cpp -o CMakeFiles/drivers__device.dir/ringbuffer.cpp.s

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o.requires:

.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o.requires

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o.provides: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o.requires
	$(MAKE) -f Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build.make Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o.provides.build
.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o.provides

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o.provides.build: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o


Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/flags.make
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o: /home/sdu/catkin_ws/src/Firmware/src/drivers/device/integrator.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sdu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__device.dir/integrator.cpp.o -c /home/sdu/catkin_ws/src/Firmware/src/drivers/device/integrator.cpp

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__device.dir/integrator.cpp.i"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sdu/catkin_ws/src/Firmware/src/drivers/device/integrator.cpp > CMakeFiles/drivers__device.dir/integrator.cpp.i

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__device.dir/integrator.cpp.s"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sdu/catkin_ws/src/Firmware/src/drivers/device/integrator.cpp -o CMakeFiles/drivers__device.dir/integrator.cpp.s

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o.requires:

.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o.requires

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o.provides: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o.requires
	$(MAKE) -f Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build.make Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o.provides.build
.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o.provides

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o.provides.build: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o


Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/flags.make
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o: /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/I2C.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sdu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__device.dir/posix/I2C.cpp.o -c /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/I2C.cpp

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__device.dir/posix/I2C.cpp.i"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/I2C.cpp > CMakeFiles/drivers__device.dir/posix/I2C.cpp.i

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__device.dir/posix/I2C.cpp.s"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/I2C.cpp -o CMakeFiles/drivers__device.dir/posix/I2C.cpp.s

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o.requires:

.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o.requires

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o.provides: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o.requires
	$(MAKE) -f Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build.make Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o.provides.build
.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o.provides

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o.provides.build: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o


Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/flags.make
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o: /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/cdev_platform.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sdu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o -c /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/cdev_platform.cpp

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.i"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/cdev_platform.cpp > CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.i

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.s"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/cdev_platform.cpp -o CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.s

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o.requires:

.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o.requires

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o.provides: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o.requires
	$(MAKE) -f Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build.make Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o.provides.build
.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o.provides

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o.provides.build: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o


Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/flags.make
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o: /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/vfile.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/sdu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/drivers__device.dir/posix/vfile.cpp.o -c /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/vfile.cpp

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/drivers__device.dir/posix/vfile.cpp.i"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/vfile.cpp > CMakeFiles/drivers__device.dir/posix/vfile.cpp.i

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/drivers__device.dir/posix/vfile.cpp.s"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/sdu/catkin_ws/src/Firmware/src/drivers/device/posix/vfile.cpp -o CMakeFiles/drivers__device.dir/posix/vfile.cpp.s

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o.requires:

.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o.requires

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o.provides: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o.requires
	$(MAKE) -f Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build.make Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o.provides.build
.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o.provides

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o.provides.build: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o


# Object files for target drivers__device
drivers__device_OBJECTS = \
"CMakeFiles/drivers__device.dir/CDev.cpp.o" \
"CMakeFiles/drivers__device.dir/ringbuffer.cpp.o" \
"CMakeFiles/drivers__device.dir/integrator.cpp.o" \
"CMakeFiles/drivers__device.dir/posix/I2C.cpp.o" \
"CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o" \
"CMakeFiles/drivers__device.dir/posix/vfile.cpp.o"

# External object files for target drivers__device
drivers__device_EXTERNAL_OBJECTS =

/home/sdu/catkin_ws/devel/lib/libdrivers__device.a: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o
/home/sdu/catkin_ws/devel/lib/libdrivers__device.a: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o
/home/sdu/catkin_ws/devel/lib/libdrivers__device.a: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o
/home/sdu/catkin_ws/devel/lib/libdrivers__device.a: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o
/home/sdu/catkin_ws/devel/lib/libdrivers__device.a: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o
/home/sdu/catkin_ws/devel/lib/libdrivers__device.a: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o
/home/sdu/catkin_ws/devel/lib/libdrivers__device.a: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build.make
/home/sdu/catkin_ws/devel/lib/libdrivers__device.a: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/sdu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX static library /home/sdu/catkin_ws/devel/lib/libdrivers__device.a"
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && $(CMAKE_COMMAND) -P CMakeFiles/drivers__device.dir/cmake_clean_target.cmake
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/drivers__device.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build: /home/sdu/catkin_ws/devel/lib/libdrivers__device.a

.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/build

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/requires: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/CDev.cpp.o.requires
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/requires: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/ringbuffer.cpp.o.requires
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/requires: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/integrator.cpp.o.requires
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/requires: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/I2C.cpp.o.requires
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/requires: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/cdev_platform.cpp.o.requires
Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/requires: Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/posix/vfile.cpp.o.requires

.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/requires

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/clean:
	cd /home/sdu/catkin_ws/build/Firmware/src/drivers/device && $(CMAKE_COMMAND) -P CMakeFiles/drivers__device.dir/cmake_clean.cmake
.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/clean

Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/depend:
	cd /home/sdu/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sdu/catkin_ws/src /home/sdu/catkin_ws/src/Firmware/src/drivers/device /home/sdu/catkin_ws/build /home/sdu/catkin_ws/build/Firmware/src/drivers/device /home/sdu/catkin_ws/build/Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Firmware/src/drivers/device/CMakeFiles/drivers__device.dir/depend

