#include <string>
#include <iostream>
#include <fstream>
#include <filesystem>

int main() {
    std::ifstream file;
    file.open("input");
    std::string line;
    
    if (! file.good()){
        return 1;
    }
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
        int data = stoi(line);
        std::cout << data << std::endl;

    }
    return 0;
}
