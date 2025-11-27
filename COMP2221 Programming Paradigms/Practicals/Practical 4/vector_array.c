#include <stdio.h>
#include <stdlib.h>

int main (int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s input_size", argv[0]);
        return 1;
    }
    int inputSize = atoi(argv[1]);
    int *a1 = calloc(inputSize, sizeof(int));
    int *a2 = calloc(inputSize, sizeof(int));

    int *result = malloc(inputSize * sizeof(int));

    for (int i=0; i < inputSize; i++) {
        result[i] = a1[i] * a2[i];
    }

    //for (int i=0; i < inputSize; i++) {
    //    printf("%d\n", result[i]);
    //}

    return 0;
}