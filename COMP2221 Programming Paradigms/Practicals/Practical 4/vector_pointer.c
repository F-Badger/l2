#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s input_size", argv[0]);
        return 1;
    }
    int inputSize = atoi(argv[1]);
    int *p1 = calloc(inputSize, sizeof(int));
    int *p2 = calloc(inputSize, sizeof(int));

    int *result = malloc(inputSize * sizeof(int));

    for (int i=0; i < inputSize; i++) {
        *(result+i) = *(p1 + i) * *(p2 + i);
    }

    free(result);

    return 0;
}