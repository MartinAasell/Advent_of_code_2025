#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
    FILE * fptr;
    fptr = fopen("day01.txt", "r");
    
    if (fptr == NULL) {
        printf("Could not open file");
        return 1;
    }

    char myString[100];
    int currentPosition = 50;
    int zeroCount = 0;

    while(fgets(myString, 100, fptr)) {
        char direction;
        int magnitude;

        if (sscanf(myString, "%c%d", &direction, &magnitude)) {
            if (direction == 'R') {
                currentPosition = (currentPosition + magnitude) % 100;
            } else if (direction == 'L') {
                currentPosition = (currentPosition - magnitude) % 100;
                if (currentPosition < 0) {
                    currentPosition += 100;
                }
            }
            if (currentPosition == 0) {
                zeroCount ++;
            }
        }
    };
    printf("Password: %d\n", zeroCount);
    fclose(fptr);
    return 0;
}