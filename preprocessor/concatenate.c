// ## is the concatenation operator

//#define USE_SINGLE_PRECISION

#ifdef USE_SINGLE_PRECISION
#define fftw_(function) fftwf_ ## function
#else
#define fftw_(function) fftw_ ## function
#endif

fftw_(complex);

// There are crazier use case scenarios, so this test really needs to be
// expanded a bit, when time permits. Meanwhile, refer
// http://stackoverflow.com/questions/1489932/c-preprocessor-and-concatenation
