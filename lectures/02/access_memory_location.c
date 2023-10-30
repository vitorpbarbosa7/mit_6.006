#include <stdio.h>

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    int *ptr = numbers; // Initialize a pointer to the start of the array

    // Access elements directly using memory addresses
    printf("Element at memory location %p: %d\n", (void*)ptr, *ptr); // Access the first element
    ptr++; // Move the pointer to the next memory location
    printf("Element at memory location %p: %d\n", (void*)ptr, *ptr); // Access the second element

    // You can also perform pointer arithmetic
    ptr += 2; // Move the pointer two positions forward
    printf("Element at memory location %p: %d\n", (void*)ptr, *ptr); // Access the fourth element

    return 0;
}
