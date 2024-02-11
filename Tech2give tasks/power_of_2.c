/* Question 3: Power of Two Write a program that takes an integer as input and 
returns true if the input is a power of two. Examples: 8=> returns true
 6=> returns false*/

#include <stdio.h>

int power_of_two(int num) {
        return (num & (num - 1)) == 0 && num != 0;
}

int main() {
	printf("8 => %s\n", power_of_two(8) ? "true" : "false");
    printf("6 => %s\n", power_of_two(6) ? "true" : "false");
    return 0;
            
}
