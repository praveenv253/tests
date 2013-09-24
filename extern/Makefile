all: testextern

testextern: main.o A.o
	g++ -o testextern main.o A.o

main.o: main.cpp A.h
	g++ -c main.cpp

A.o:
	g++ -c A.cpp

