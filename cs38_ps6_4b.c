#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <math.h>

#define PI 3.141592653589793238462
const int L = 20;


//Uses branch and bound recursively to find maxf value and adds to file
double branch_search(double currentsum, int l, double z_value, int currentL,\
   double greatest){
  double maxf = greatest;

  //if leaf
  if (currentL == l){
    if (currentsum > maxf){
      maxf = currentsum;
    }
    return maxf;
  }

  double child1 = ((3 * z_value) / 2) - floor((3 * z_value) / 2);
  double child2 = ((3 * z_value + 1) / 2) - floor((3 * z_value + 1) / 2);

  double futuresum1 = currentsum + (cos(2 * PI * child1));
  double futuresum2 = currentsum + (cos(2 * PI * child2));

  //if statements are for truncation
  if (futuresum1 >= maxf || currentL != l + 1){
      maxf = branch_search(currentsum + (cos(2 * PI * child1)), l + 1, child1, currentL, maxf);
  }

  if (futuresum2>= maxf || currentL != l + 1){
    maxf = branch_search(currentsum + (cos(2 * PI * child2)), l + 1, child2, currentL, maxf);
  }
  return maxf;
 }

int main(void){
  FILE *fptr = fopen("submissiontryB.txt", "w");
  fprintf(fptr, "%d, %f, %f\n", 1, -1.0, 0.0);
  for (int i = 2; i <= L; i ++){
    double maxf = -1.0;     //maxf being f_l * l
    clock_t start = clock();
    // start at l = 2 and branch with root 3/4
    maxf = branch_search(-1.0, 2, 0.75, i, maxf);
    clock_t stop = clock();
    double runtime = (double)(stop - start) / CLOCKS_PER_SEC;
    fprintf(fptr, "%d, %f, %f\n", i, maxf / i, runtime);
  }
  fclose(fptr);
  return 0;
}
