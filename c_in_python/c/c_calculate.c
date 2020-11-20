#include <stdio.h>

int calculate(long number){
    int result = 1;
    for (int i = 0; i <number; i++)
    {
        result = result + 1;
        result = result - 1;
    }
    return result;
}