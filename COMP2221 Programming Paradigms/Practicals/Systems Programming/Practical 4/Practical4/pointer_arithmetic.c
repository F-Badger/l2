#include <stdio.h>

int main () {
    int myArray[] = {0,1,2,3,4};
    int *p = &myArray[0];  // point to first element of array
    for (int i = 0; i < 5; i++) {
        printf("Element: %d, Address: %p\n", *p, p); // output element and its address
        p++; // increment pointer to next element
             // address differs by 4 bytes, since sizeof(int) = 4
    }
    return 0;
}