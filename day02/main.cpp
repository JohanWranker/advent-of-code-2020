#include <string>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include <bits/stdc++.h>
#include <regex>

using namespace std;

int main() {
    ifstream file;
    file.open("../../input");
    string line;
    std::vector<int> list = {};
    
    if (! file.good()){
        cout << "file not found" << endl;
        return 1;
    }
    int count = 0;
    while (getline(file, line)) {
        
        std::regex re("(\\d+)-(\\d+)\\s+(\\w):\\s+(\\w+)");
        smatch match;
        regex_search(line, match, re);

        int low = stoi(match.str(1));
        int high = stoi(match.str(2));
        string c = match.str(3);
        auto data = match.str(4);
        int countInstance = 0;
        for (int i = 0; i < data.size(); i++){
            if (data[i] == c[0] ) {
                countInstance++;
            }
        }
        if (countInstance >= low && countInstance <= high) {
            count++;
        }
      cout << count << endl;
    }
    file.close();
    file.open("../../input");
    count = 0;
    while (getline(file, line)) {
        std::regex re("(\\d+)-(\\d+)\\s+(\\w):\\s+(\\w+)");
        smatch match;
        bool ok = false;
        regex_search(line, match, re);
        int pos1 = stoi(match.str(1));
        int pos2 = stoi(match.str(2));
        string c = match.str(3);
        auto data = match.str(4);
        if (data[pos1-1] == c[0]) {
            ok = ! ok;
        } 
        if (data[pos2-1] == c[0]) {
            ok = ! ok;
        }
        if (ok) {
            count++;
        }
        cout << count << endl;
    }
    return 1;
}
