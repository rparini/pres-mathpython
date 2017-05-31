#include <vector>
#include <math.h>
#include <iostream>

std::vector<int> sieve_of_eratosthenes(int n){
	std::vector<int> primes;
	primes.reserve(n/2);
	std::vector<bool> A(n+1, true);

	for (int i = 2; i <= (int)sqrt(n); i++) {
		if (A[i]) {
			// i is a prime so append it to primes
			primes.push_back(i);

			for (int j = i*i; j <= n; j += i) {
				A[j] = false;
			}
		}
	}

	// return indices from sqrt(n) to n that are primes
	// these were not already covered in the original loop
	for (int i = (int)sqrt(n)+1; i <= n; i++) {
		if (A[i]) {
			// append i to primes
			primes.push_back(i);
		}
	}

	return primes;
}

int main() {
	std::vector<int> primeList = sieve_of_eratosthenes(47);

	for (int i=0; i < primeList.size(); i++){
  		std::cout << primeList[i] << ' ';
	}
}