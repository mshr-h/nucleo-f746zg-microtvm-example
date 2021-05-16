# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.13.1)

find_package(Zephyr HINTS $ENV{ZEPHYR_BASE})
project(microtvm_zephyr_runtime)

set(CMAKE_VERBOSE_MAKEFILE ON)
file(GLOB_RECURSE TVM_CRT_SOURCES model-metadata.c model.c crt/*.c *.cc)
target_sources(app PRIVATE src/main.c ${TVM_CRT_SOURCES})

get_filename_component(CMSIS_5_PATH "3rdparty/CMSIS_5" ABSOLUTE)
message(STATUS "CMSIS PATH ${CMSIS_5_PATH}")
target_include_directories(app PRIVATE crt-config)
target_include_directories(app SYSTEM PRIVATE
    crt/include
    "${CMSIS_5_PATH}/CMSIS/DSP/Include"
    "${CMSIS_5_PATH}/CMSIS/NN/Include"
)
