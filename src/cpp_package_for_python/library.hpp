#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include <vector>
#include <algorithm>

namespace py = pybind11;

int add(const int &, const int &);

pybind11::object find_index(const std::vector<int>& items, int value);