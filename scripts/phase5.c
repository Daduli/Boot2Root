#include <stdio.h>

char array_123[16] = { 105, 115, 114, 118, 101, 97, 119, 104, 111, 98, 112, 110, 117, 116, 102, 103 }; // weak

int main(int ac, char **av)
{
    int index = av[1][0] & 0xF;
    printf("Index: %d | Character: %c\n", index, array_123[index]);
}