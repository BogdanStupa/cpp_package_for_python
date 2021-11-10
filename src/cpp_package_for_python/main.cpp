#include <pybind11/pybind11.h>
#include "library.hpp" 

namespace py = pybind11;

PYBIND11_MODULE(cpp_package_for_python, m) {
    m.def("add", &add); 
    m.def("find_index", &find_index);
};