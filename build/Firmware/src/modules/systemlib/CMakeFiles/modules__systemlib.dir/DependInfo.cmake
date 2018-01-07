# The set of languages for which implicit dependencies are needed:
set(CMAKE_DEPENDS_LANGUAGES
  "C"
  "CXX"
  )
# The set of files for implicit dependencies of each language:
set(CMAKE_DEPENDS_CHECK_C
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/airspeed.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/airspeed.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/board_serial.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/board_serial.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/bson/tinybson.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/bson/tinybson.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/conversions.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/conversions.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/cpuload.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/cpuload.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/crc.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/crc.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/hx_stream.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/hx_stream.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/mavlink_log.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/mavlink_log.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/otp.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/otp.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/perf_counter.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/perf_counter.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/pid/pid.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/pid/pid.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/print_load_posix.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/print_load_posix.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/pwm_limit/pwm_limit.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/pwm_limit/pwm_limit.c.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/rc_check.c" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/rc_check.c.o"
  )
set(CMAKE_C_COMPILER_ID "GNU")

# Preprocessor definitions for this target.
set(CMAKE_TARGET_DEFINITIONS_C
  "BUILD_URI=localhost"
  "CONFIG_ARCH_BOARD_SITL"
  "MODULE_NAME=\"modules__systemlib\""
  "ROSCONSOLE_BACKEND_LOG4CXX"
  "ROS_BUILD_SHARED_LIBS=1"
  "ROS_PACKAGE_NAME=\"Project\""
  "__DF_LINUX"
  "__PX4_LINUX"
  "__PX4_POSIX"
  "__STDC_FORMAT_MACROS"
  "noreturn_function=__attribute__((noreturn))"
  )

# The include file search paths:
set(CMAKE_C_TARGET_INCLUDE_PATH
  "Firmware"
  "Firmware/src"
  "Firmware/src/modules"
  "/home/sdu/catkin_ws/src/Firmware/src"
  "/home/sdu/catkin_ws/src/Firmware/src/drivers/boards/sitl"
  "/home/sdu/catkin_ws/src/Firmware/src/include"
  "/home/sdu/catkin_ws/src/Firmware/src/lib"
  "/home/sdu/catkin_ws/src/Firmware/src/lib/DriverFramework/framework/include"
  "/home/sdu/catkin_ws/src/Firmware/src/lib/matrix"
  "/home/sdu/catkin_ws/src/Firmware/src/modules"
  "/home/sdu/catkin_ws/src/Firmware/src/platforms"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib"
  "/home/sdu/catkin_ws/src/Firmware/src/platforms/posix/include"
  "/home/sdu/catkin_ws/src/Firmware/mavlink/include/mavlink"
  "Firmware/external/Install/include"
  )
set(CMAKE_DEPENDS_CHECK_CXX
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/battery.cpp" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/battery.cpp.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/circuit_breaker.cpp" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/circuit_breaker.cpp.o"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib/hysteresis/hysteresis.cpp" "/home/sdu/catkin_ws/build/Firmware/src/modules/systemlib/CMakeFiles/modules__systemlib.dir/hysteresis/hysteresis.cpp.o"
  )
set(CMAKE_CXX_COMPILER_ID "GNU")

# Preprocessor definitions for this target.
set(CMAKE_TARGET_DEFINITIONS_CXX
  "BUILD_URI=localhost"
  "CONFIG_ARCH_BOARD_SITL"
  "MODULE_NAME=\"modules__systemlib\""
  "ROSCONSOLE_BACKEND_LOG4CXX"
  "ROS_BUILD_SHARED_LIBS=1"
  "ROS_PACKAGE_NAME=\"Project\""
  "__DF_LINUX"
  "__PX4_LINUX"
  "__PX4_POSIX"
  "__STDC_FORMAT_MACROS"
  "noreturn_function=__attribute__((noreturn))"
  )

# The include file search paths:
set(CMAKE_CXX_TARGET_INCLUDE_PATH
  "Firmware"
  "Firmware/src"
  "Firmware/src/modules"
  "/home/sdu/catkin_ws/src/Firmware/src"
  "/home/sdu/catkin_ws/src/Firmware/src/drivers/boards/sitl"
  "/home/sdu/catkin_ws/src/Firmware/src/include"
  "/home/sdu/catkin_ws/src/Firmware/src/lib"
  "/home/sdu/catkin_ws/src/Firmware/src/lib/DriverFramework/framework/include"
  "/home/sdu/catkin_ws/src/Firmware/src/lib/matrix"
  "/home/sdu/catkin_ws/src/Firmware/src/modules"
  "/home/sdu/catkin_ws/src/Firmware/src/platforms"
  "/home/sdu/catkin_ws/src/Firmware/src/modules/systemlib"
  "/home/sdu/catkin_ws/src/Firmware/src/platforms/posix/include"
  "/home/sdu/catkin_ws/src/Firmware/mavlink/include/mavlink"
  "Firmware/external/Install/include"
  )

# Targets to which this target links.
set(CMAKE_TARGET_LINKED_INFO_FILES
  )

# Fortran module output directory.
set(CMAKE_Fortran_TARGET_MODULE_DIR "")
