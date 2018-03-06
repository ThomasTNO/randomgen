/*
 * Generate testing csv files
 *
 * GCC only
 *
 *  gcc xoroshiro128-test-data-gen.c xoroshiro128plus.orig.c /
 * ../splitmix64/splitmix64.c -o xoroshiro128-test-data-gen
 *  ./xoroshiro128-test-data-gen
 *
 */

#include "../splitmix64/splitmix64.h"
#include "pcg64.orig.h"
#include <inttypes.h>
#include <stdio.h>

#define N 1000

typedef uint64_t __uint128_t;

int main() {
  pcg64_random_t c;
  uint64_t state, seed = 0xDEADBEAF;
  state = seed;
  __uint128_t temp;
  rng.state = (__uint128_t)splitmix64_next(&state) << 64;
  rng.state |= splitmix64_next(&state);
  rng.inc = (__uint128_t)1;
  int i;
  uint64_t store[N];
  for (i = 0; i < N; i++) {
    store[i] = pcg64_random_r(&rng);
    ;
  }

  FILE *fp;
  fp = fopen("pcg64-testset-1.csv", "w");
  if (fp == NULL) {
    printf("Couldn't open file\n");
    return -1;
  }
  fprintf(fp, "seed, 0x%" PRIx64 "\n", seed);
  for (i = 0; i < N; i++) {
    fprintf(fp, "%d, 0x%" PRIx64 "\n", i, store[i]);
    if (i == 999) {
      printf("%d, 0x%" PRIx64 "\n", i, store[i]);
    }
  }
  fclose(fp);

  uint64_t state, seed = 0;
  state = seed;
  rng.state =
      (__uint128_t)splitmix64_next(&state) << 64 | splitmix64_next(&state);
  rng.inc = (__uint128_t)1;
  for (i = 0; i < N; i++) {
    store[i] = pcg64_random_r(&rng);
    ;
  }
  fp = fopen("xoroshiro128-testset-2.csv", "w");
  if (fp == NULL) {
    printf("Couldn't open file\n");
    return -1;
  }
  fprintf(fp, "seed, 0x%" PRIx64 "\n", seed);
  for (i = 0; i < N; i++) {
    fprintf(fp, "%d, 0x%" PRIx64 "\n", i, store[i]);
    if (i == 999) {
      printf("%d, 0x%" PRIx64 "\n", i, store[i]);
    }
  }
  fclose(fp);
}