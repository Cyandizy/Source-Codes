#include <iostream>
#include "upper.hpp"

std::string upper(std::string str) {
    std::string upperCased;
    for (char ch : str) {
        upperCased += static_cast<char>(toupper(ch));
    }
    upperCased;
    return upperCased;
}