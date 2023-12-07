#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

struct Range {
	int dest;
	int src;
	int range;
	friend ostream& operator<<(ostream& os, const Range& src);
};
ostream& operator<<(ostream& os, const Range& src) {
	os << src.dest << " " << src.src << " " << src.range;
	return os;
}

struct SeedStruct {
	int * seeds;
	int count;
	friend ostream& operator<<(ostream& os, const SeedStruct& ss);
};
ostream& operator<<(ostream& os, const SeedStruct& ss) {
	for(int i=0;i<ss.count;i++) {
		os << ss.seeds[i] << " ";
	}
	return os;
}

SeedStruct* handle_seeds(char * buffer) {
	// this is destroyed during the strtok
	// calls
	char line[255];
	strcpy(line,buffer);
	char * token = strtok(line," ");
	int token_count = 0;
	while (token) {
		token_count++;
		//cout << token << "\n";
		token = strtok(0," ");
	}
	//cout << "token count: " << token_count << "\n";
	int *seeds = new int[token_count-1];
	int index = 0;
	strcpy(line,buffer);
	token = strtok(line," ");
	while (token) {
		int res = strncmp(token,"seeds:",6);
		if (res==0) {
			token = strtok(0," ");
			continue;
		}
		seeds[index] = atoi(token);
		index++;
		//cout << "token: " << token << "\n";
		token = strtok(0," ");
	}

	for(int i=0;i<4;i++) {
		//cout << "FINAL " << seeds[i] << "\n";
	}
	SeedStruct * ss = new SeedStruct;
	ss->count = token_count-1;
	ss->seeds = seeds;
	return ss;
}

Range* handle_range(char * buffer) {
	char line[255];
	strcpy(line,buffer);
	cout << "handle range line is now: " << line << "\n";
	Range * range = new Range;
	char * token = strtok(line," ");
	range->dest = atoi(token);
	token = strtok(0," ");
	range->src = atoi(token);
	token = strtok(0," ");
	range->range = atoi(token);
	return range;
}

int main() {

	enum State { start, seed_to_soil, soil_to_fert, fert_to_water,
       	water_to_light, light_to_temp, temp_to_humid, humid_to_loc};

	State state = start;
	SeedStruct * seeds;

	// read file
	char buffer[255];
	ifstream inf;
	inf.open("sample.txt");
	while (!inf.eof()) {
		inf.getline(buffer,255);
		if (strlen(buffer)==0) {
			continue;
		}
		cout << "line read from file: " << strlen(buffer) << " --> " << buffer << "\n";
		if (strncmp("seeds:",buffer,5)==0) {
			cout << "seeds matched" << "\n";
			seeds = handle_seeds(buffer);
			continue;
		}
		if (strncmp("seed-to-soil map:",buffer,17)==0) {
			cout << "change state to seed to soil" << "\n";
			state = seed_to_soil;
			continue;
		}
		if (strncmp("soil-to-fertilizer map:",buffer,23)==0) {
			cout << "change state to soil to fert" << "\n";
			state = soil_to_fert;
			continue;
		}
		if (strncmp("fertilizer-to-water map:",buffer,24)==0) {
			cout << "change state to fert to water" << "\n";
			state = fert_to_water;
			continue;
		}
		if (strncmp("water-to-light map:",buffer,19)==0) {
			cout << "change state to water to light" << "\n";
			state = water_to_light;
			continue;
		}
		if (strncmp("light-to-temperature map:",buffer,25)==0) {
			cout << "change state light to temp" << "\n";
			state = light_to_temp;
			continue;
		}
		if (strncmp("temperature-to-humidity map:",buffer,28)==0) {
			cout << "change state temp to humid" << "\n";
			state = temp_to_humid;
			continue;
		}
		if (strncmp("humidity-to-location map:",buffer,25)==0) {
			cout << "change state humid to loc" << "\n";
			state = humid_to_loc;
			continue;
		}

		Range* range = handle_range(buffer);
		cout << "parsed range: " << *range << "\n";
	}
	inf.close();

	cout << "seeds: " << *seeds << "\n";
	return 0;
}
