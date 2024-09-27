#include <stdio.h>
#include <stdlib.h>

int func4(int a1)
{
  int v1; // esi

  if ( a1 <= 1 )
    return 1;
  v1 = func4(a1 - 1);
  return v1 + func4(a1 - 2);
}

int main(int ac, char **av)
{
    printf("Result: %d\n", func4(atoi(av[1])));
}