#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>

using namespace std;

struct Range {
    int dest;
    int src;
    int range;
};

int find_num(int target, int rcount, Range *ranges) {
    for(int i=0;i<rcount;i++) {
        Range r = ranges[i];
        if ((target>=r.src) && (target<=r.src+r.range)) {
            return r.dest + ( target - r.src);
        }
    }
    return target;
}

void test1() {
    Range ranges[2] = {
        Range{50,98,2},
        Range{52,50,48}
    };

    int res = find_num(79,2,ranges);
    cout << "res: " << res << "\n";
}

void print_int_array(int* a,int count) {
    for(int i=0;i<count;i++) {
        cout << a[i] << " ";
    }
    cout << "\n";
}

void handle_seeds(char * line) {
    vector<int> svec;
    cout << line << "\n";
    int token_count = 0;
    char * token = strtok(line," ");
    while (token) {
        if (strcmp(token,"seeds:")==0) {

        } else {
            token_count++;
            cout << "first loop token: " << token << "\n";
            svec.push_back(atoi(token));
        }
        token = strtok(0, " ");
    }
    cout << "total seeds: " << token_count << "\n";
    int * seeds_array = new int[token_count];
    token = strtok(line," ");
    token_count = 0;
    while (token) {
        cout << "token at top of loop: " << token << "\n";
        if (strcmp(token,"seeds:")==0) {

        } else {
            cout << "setting into array..." << "\n";
            seeds_array[token_count] = atoi(token);
            token_count++;
            cout << "token: " << token << "\n";
        }
        token = strtok(0, " ");
        cout << "token is now " << token << "\n";
    }
    //print_int_array(seeds_array,4);
    for(auto i=svec.begin();i<svec.end();i++) {
        cout << "from vec: " << *i << "\n";
    }
}

int main() {

    ifstream inf("sample.txt");
    if (!inf) {
        cout << "unable to open file\n";
        return -1;
    }

    int *seeds_array = 0;

    char line[512]; // up to 512 chars
    while (inf) {
        inf.getline(line,512);
        if (strncmp(line,"seeds:",5)==0) {
            handle_seeds(line);
        }
    }


    delete[] seeds_array;
    return 0;
}
