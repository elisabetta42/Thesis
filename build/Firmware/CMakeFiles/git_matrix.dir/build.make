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

# Utility rule file for git_matrix.

# Include the progress variables for this target.
include Firmware/CMakeFiles/git_matrix.dir/progress.make

Firmware/CMakeFiles/git_matrix: Firmware/git_init_src_lib_matrix.stamp


Firmware/git_init_src_lib_matrix.stamp: /home/sdu/catkin_ws/src/Firmware/.gitmodules
Firmware/git_init_src_lib_matrix.stamp: /home/sdu/catkin_ws/src/Firmware/src/lib/matrix/.git
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/sdu/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "git submodule src/lib/matrix"
	cd /home/sdu/catkin_ws/src/Firmware && bash /home/sdu/catkin_ws/src/Firmware/Tools/check_submodules.sh src/lib/matrix
	cd /home/sdu/catkin_ws/src/Firmware && cmake -E touch /home/sdu/catkin_ws/build/Firmware/git_init_src_lib_matrix.stamp

git_matrix: Firmware/CMakeFiles/git_matrix
git_matrix: Firmware/git_init_src_lib_matrix.stamp
git_matrix: Firmware/CMakeFiles/git_matrix.dir/build.make

.PHONY : git_matrix

# Rule to build all files generated by this target.
Firmware/CMakeFiles/git_matrix.dir/build: git_matrix

.PHONY : Firmware/CMakeFiles/git_matrix.dir/build

Firmware/CMakeFiles/git_matrix.dir/clean:
	cd /home/sdu/catkin_ws/build/Firmware && $(CMAKE_COMMAND) -P CMakeFiles/git_matrix.dir/cmake_clean.cmake
.PHONY : Firmware/CMakeFiles/git_matrix.dir/clean

Firmware/CMakeFiles/git_matrix.dir/depend:
	cd /home/sdu/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sdu/catkin_ws/src /home/sdu/catkin_ws/src/Firmware /home/sdu/catkin_ws/build /home/sdu/catkin_ws/build/Firmware /home/sdu/catkin_ws/build/Firmware/CMakeFiles/git_matrix.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Firmware/CMakeFiles/git_matrix.dir/depend
