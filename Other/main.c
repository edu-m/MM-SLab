// montecarlo approach to integral evaluation
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double f(double x) { // function we want to evaluate
  return exp(-pow(x, 2) / 2) / sqrt(2 * M_PI);
}

int main() {
  srand(time(NULL));
  double a = 0.5;
  double b = 2;
  double M = 0;
  int NS = 0;
  int granularity = 1000;
  int tries = 10000000;
  double stepping = (b - a) / granularity;

  double *linspace = malloc((granularity + 1) * sizeof(double));
  for (int i = 0; i <= granularity; i++) {
    linspace[i] = f((stepping * i) + a);
    if (linspace[i] > M)
      M = linspace[i];
  }
  double xi, eta, r1, r2;
  for (int i = 0; i < tries; i++) {
    r1 = ((double)rand()) / RAND_MAX;
    r2 = ((double)rand()) / RAND_MAX;
    xi = a + r1 * (b - a);
    eta = r2 * M;
    NS += (eta <= f(xi));
  }
  double p = (double)NS / (double)tries;
  double I = p * M * (b - a);
  printf("%f\n", I);
}