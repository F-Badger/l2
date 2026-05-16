# Results

## Timing Table

|  | 1000 | 1000000 | 1000000 | 1000000000000
|----------|----------|----------|----------|----------|
| ./vector_array| 0.002189s | 0.002152s   | 0.002160s | 0.002198s |
| ./vector_pointer| 0.002148s | 0.002200s | 0.002217s | 0.002167s |

Each configuration was run 1000 times. 

Times seem to vary with no obvious pattern. Using pointers was faster for the smallest and largest input size; using an array was quicker for the two intermediate input sizes, although it should be noted that times are extremely close with no practical difference. This reveals both memory traversal methods in C are generally comparably efficient. 