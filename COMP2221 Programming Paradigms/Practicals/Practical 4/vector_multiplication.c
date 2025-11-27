#include <stdio.h>
#include <stdlib.h>

int main () {
    int array1[] = {3,4,5};
    int array2[] = {2,2,8};

    int *p1 = array1;
    int *p2 = array2;

    size_t len1 = sizeof(array1) / sizeof(int);
    size_t len2 = sizeof(array2) / sizeof(int);

    if (len1 != len2) {
        printf("Input arrays must have equal length");
        return 1;
    }

    int *result = malloc(len1 * sizeof(int));

    for (int i=0; i < len1; i++) {
        *(result+i) = *(p1 + i) * *(p2 + i);
    }

    for (int i=0; i < len1; i++) {
        printf("%d\n", *(result+i));
    }

    free(result);

    return 0;
}