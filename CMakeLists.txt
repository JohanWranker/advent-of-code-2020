cmake_minimum_required(VERSION 3.15)
project("AoC-2020")

configure_file(input ${CMAKE_CURRENT_BINARY_DIR}/input)
add_subdirectory("day01")
add_subdirectory("day02")