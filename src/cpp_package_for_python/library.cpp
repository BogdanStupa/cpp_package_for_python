#include "library.hpp"


int add(const int &a, const int &b) {
    return a + b;
}


py::object find_index(const std::vector<int>& items, int value) {
    auto ptr = std::find(items.begin(), items.end(), value);
    if (ptr != items.end()) {
        return py::cast(ptr - items.begin());
    } else {
        return py::none();
    }
}