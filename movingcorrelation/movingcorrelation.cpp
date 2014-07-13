#include <iostream>
#include <fstream>
#include <complex>
#include <cmath>
#define PREAMBLE_LENGTH 64
#define PACKET_THRESHOLD 0.1

using namespace std;

void save_complex_array_binary(const char *filename, complex<float> *data,
							   int num_elements)
{
	fstream f(filename, fstream::out | fstream::binary);
	f.write((char *)data, sizeof(complex<float>) * num_elements);
	f.close();
}

int main()
{
	int tmax = 1e6;
	complex<float> *input_data = new complex<float>[tmax];
	fstream f("data.bin", fstream::in | fstream::binary);
	f.read((char *)input_data, sizeof(complex<float>) * tmax);
	f.close();
	
	int peak_index = 0;
	double peak_value = 0;
	int _packet_found = 0;
	int *packet_found = &_packet_found;

	int n = PREAMBLE_LENGTH / 2;	// Each half window is half the
									// size of the preamble
	float abs1, abs2;
	complex<float> *abs;
	abs = new complex<float>[tmax];

	float corr_coeff, temp1 = 0;

	complex<float> left_avg_old(0, 0);
	complex<float> right_avg_old(0, 0);
	complex<float> left_avg_new(0, 0);
	complex<float> right_avg_new(0, 0);
	complex<float> *left_avg;
	complex<float> *right_avg;
	left_avg = new complex<float>[tmax];
	right_avg = new complex<float>[tmax];

	complex<float> cross_corr(0, 0);
	float auto_corr_left = 0.0;
	float auto_corr_right = 0.0;

	bool crossed_threshold = false;
	int max_time_steps_after_threshold = 64;
	int count_after_threshold = 0;

	//complex<float> *found_packets;
	//found_packets = (complex<float> *) calloc(tmax, sizeof(complex<float>));

	int i;
	for(i = 0; i < tmax && count_after_threshold < max_time_steps_after_threshold; i++) {
		if(i == 0) {
			// First calculate the average for the left and right sides
			int j;
			for(j = 0; j < n; j++) {
				left_avg_old += input_data[j] / float(n);
				right_avg_old += input_data[n+j] / float(n);
			}
			left_avg[0] = left_avg_old;
			right_avg[0] = right_avg_old;
			// Then correlate the left and right halves, minus the respective averages
			for(j = 0; j < n; j++) {
				cross_corr += (input_data[j] - left_avg_old) * conj(input_data[n+j] - right_avg_old);
				auto_corr_left += norm(input_data[j] - left_avg_old);
				auto_corr_right += norm(input_data[j+n] - right_avg_old);
				/*cross_corr = gsl_complex_add(cross_corr, gsl_complex_mul(input_data[j], gsl_complex_conjugate(input_data[j+n])));*/
				/*auto_corr_left += gsl_complex_abs2(input_data[j]);*/
				/*auto_corr_right += gsl_complex_abs2(input_data[j]);*/
			}
		} else {
			left_avg_new = left_avg_old + input_data[i-1+n] / float(n) - input_data[i-1] / float(n);
			right_avg_new = right_avg_old + input_data[i-1+2*n] / float(n) - input_data[i-1+n] / float(n);
			left_avg[i] = left_avg_new;
			right_avg[i] = right_avg_new;

			cross_corr += (input_data[i-1+n] - left_avg_old) * conj(input_data[i-1+2*n] - right_avg_new)
						  - (input_data[i-1] - left_avg_old) * conj(input_data[i-1+n] - right_avg_new);
			auto_corr_left += norm(input_data[i-1+n]) - norm(input_data[i-1])
							  - real(left_avg_new * conj(input_data[i-1+n] - input_data[i-1]))
							  - real(conj(left_avg_old) * (input_data[i-1+n] - input_data[i-1]));
			//auto_corr_left += gsl_complex_abs2(input_data[i-1+n]) - gsl_complex_abs2(input_data[i-1])
			//                  - GSL_REAL(gsl_complex_mul(left_avg_new, gsl_complex_conjugate(gsl_complex_sub(input_data[i-1+n], input_data[i-1]))))
			//                  - GSL_REAL(gsl_complex_mul(gsl_complex_conjugate(left_avg_old), gsl_complex_sub(input_data[i-1+n], input_data[i-1])));
			auto_corr_right += norm(input_data[i-1+2*n]) - norm(input_data[i-1+n])
							   - real(right_avg_new * conj(input_data[i-1+2*n] - input_data[i-1+n]))
							   - real(conj(right_avg_old) - (input_data[i-1+2*n] - input_data[i-1+n]));
			//auto_corr_right += gsl_complex_abs2(input_data[i-1+2*n]) - gsl_complex_abs2(input_data[i-1+n])
			//                   - GSL_REAL(gsl_complex_mul(right_avg_new, gsl_complex_conjugate(gsl_complex_sub(input_data[i-1+2*n], input_data[i-1+n]))))
			//                   - GSL_REAL(gsl_complex_mul(gsl_complex_conjugate(right_avg_old), gsl_complex_sub(input_data[i-1+2*n], input_data[i-1+n])));
			//cross_corr = gsl_complex_add(cross_corr, gsl_complex_mul(input_data[i+n-1], gsl_complex_conjugate(input_data[i+2*n-1])));
			//cross_corr = gsl_complex_sub(cross_corr, gsl_complex_mul(input_data[i-1], gsl_complex_conjugate(input_data[i+n-1])));
			//auto_corr_left += gsl_complex_abs2(input_data[i+n-1]) - gsl_complex_abs2(input_data[i-1]);
			//auto_corr_right += gsl_complex_abs2(input_data[i+2*n-1]) - gsl_complex_abs2(input_data[i+n-1]);
			
			left_avg_old = left_avg_new;
			right_avg_old = right_avg_new;
		}

		abs1 = std::abs(cross_corr);
		if(abs1 < 1e-5) {
			//cross_corr = complex<float>(0, 0);
			abs2 = 0;
			corr_coeff = 0;
		} else {
			abs2 = sqrt(auto_corr_left * auto_corr_right);
			corr_coeff = abs1 / abs2;
		}
		abs[i] = complex<float>(abs1, abs2);

		// To find postion of maximum correlation
		if(fabs(1 - corr_coeff) < fabs(1 - peak_value)) {	// If the new corr_coeff is closer to 1 than the old peak_value
			peak_value = corr_coeff;
			peak_index = i;
			if(!crossed_threshold && (peak_value >= 1 - PACKET_THRESHOLD) && (peak_value <= 1 + PACKET_THRESHOLD)) {
				crossed_threshold = true;
			}
		}
		if(crossed_threshold) {
			//count_after_threshold++;
		}
	}

	save_complex_array_binary("input_data.out", input_data, tmax);
	save_complex_array_binary("abs.out", abs, tmax);
	save_complex_array_binary("left_avg_new.out", left_avg, tmax);
	save_complex_array_binary("right_avg_new.out", right_avg, tmax);

	//if((peak_value >= 1 - PACKET_THRESHOLD) && (peak_value <= 1 + PACKET_THRESHOLD)) {
	//    *packet_found = 1;
	//}

	//if(*packet_found) {
	//    GSL_SET_COMPLEX(found_packets + peak_index, 1, 0);
	//    temp1 = 0;
	//    for(i = peak_index; i < peak_index + n; i++) {
	//        temp1 += gsl_complex_arg(gsl_complex_mul_real(gsl_complex_mul(input_data[i], gsl_complex_conjugate(input_data[i+n])), -1));
	//    }
	//    *freq_est = temp1 / (2 * M_PI * n * n);
	//}

	//save_complex_array_binary("found_packets.out", found_packets, tmax, 1);

	return 0;
}
