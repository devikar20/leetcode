#include <stdio.h>

int main() {
    int number = 42;
    // Creating a pointer variable that stores the hardware address of 'number'
    int *pointer = &number; 

    printf("Success! The C compiler is working cleanly.\n");
    printf("Value of number: %d\n", number);
    printf("Memory address of number where it lives in RAM: %p\n", (void*)pointer);
    return 0;
}