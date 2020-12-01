#include <string>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream file;
    file.open("input");
    string line;
    std::vector<int> list = {};
    
    if (! file.good()){
        cout << "file not found" << endl;
        return 1;
    }
    while (getline(file, line)) {
        int data = stoi(line);
        list.push_back(data);
    }
    std::sort(list.begin(), list.end()); 
    for (int i : list) {
        for (int j : list) {
            for (int k : list) {
                cout << i+j+k <<endl;
                if (i+j+k == 2020) {
                    cout << i*j*k <<endl;
                    cout << i <<endl;
                    cout << j <<endl;
                    cout << k <<endl;
                    return 0;
                }
                if (i+j+k > 2020) {
                    break;
                }
            }
        }
    }
    cout << "fail" << endl;
    
    return 1;
}
