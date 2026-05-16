#include <stdlib.h>
#include <stdio.h>

void allocateInt(int **p) {
    // double pointer needed so that the function can change the value of ptr from main()
    *p = malloc(sizeof(int)); // *p is ptr; sets ptr to the address of the allocated memory
    // p is a local variable and holds the address of ptr (&ptr); it exists on the stack
    if (*p == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }

    // set value of integer (on the heap)
    **p = 10;
}

int main() {
    int *ptr = NULL; // ptr exists on the stack; it will point to the address of the int (after allocation)
    
    printf("Before allocation, ptr = %p\n", ptr);

    allocateInt(&ptr);

    printf("After allocation, ptr = %p\n", ptr);
    printf("Value at allocated memory: %d\n", *ptr);
    // *ptr is the integer and exists on the heap

    // necessary to release memory so prevent memory leaks
    free(ptr);

    return 0;
}