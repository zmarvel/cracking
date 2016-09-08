#include <stdio.h>
#include <stdlib.h>

void main(int argc, char* argv[]){
  printf("testing 3: %i\n", count(3, 0));
  printf("testing 4: %i\n", count(4, 0));
  printf("testing 5: %i\n", count(5, 0));
  printf("testing 6: %i\n", count(6, 0));
}

int count(int num_stair, int counter){
  if (num_stair < 0) return 0;
  else if (num_stair == 3) return 4;
  else if (num_stair < 3) return num_stair;
  return (count(num_stair - 1, counter + 1) + count(num_stair - 2, counter + 1) + count(num_stair - 3, counter + 1));
}
