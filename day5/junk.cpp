#include <iostream>
#include <fstream>
#include <cstring>

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
    cout << line << "\n";
    int token_count = 0;
    char * token = strtok(line," ");
    while (token) {
        if (strcmp(token,"seeds:")==0) {

        } else {
            token_count++;
            //cout << "token: " << token << "\n";
        }
        token = strtok(0, " ");
    }
    cout << "total seeds: " << token_count << "\n";
    int * seeds_array = new int[token_count];
    token = strtok(line," ");
    token_count = 0;
    while (token) {
        if (strcmp(token,"seeds:")==0) {

        } else {
            seeds_array[token_count] = atoi(token);
            token_count++;
            cout << "token: " << token << "\n";
        }
        token = strtok(0, " ");
    }
    print_int_array(seeds_array,4);

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
