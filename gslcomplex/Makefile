LIBS = -lgsl -lfftw3 -lgslcblas -lm -luhd -lboost_program_options -lboost_thread -lplplotd -lpthread

all: simple float double int

simple: simple.cpp
	g++ -O3 simple.cpp -o simple $(LIBS)

float: gsl_complex_float_vs_std_complex_float.cpp
	g++ -std=c++0x -Ofast -march=native gsl_complex_float_vs_std_complex_float.cpp -o float $(LIBS)

double: gsl_complex_double_vs_std_complex_double.cpp
	g++ -std=c++0x -Ofast -march=native gsl_complex_double_vs_std_complex_double.cpp -o double $(LIBS)

int: std_complex_int.cpp
	g++ -std=c++0x -Ofast -march=native std_complex_int.cpp -o int $(LIBS)
clean:
	rm -rf simple float double
