#include <stdio.h>

int array[1001];

int main(void) {
    int number, i, j, temp;
    scanf("%d", &number);
    for(i = 0; i < number; i++) {
        scanf("%d", &array[i]);
    }
    
    for(i = 0; i < number - 1; i ++) {
        j = i;
        while(j >= 0 && array[j] > array[j + 1]) {
            temp = array[j];
            array[j] = array[j + 1];
            array[j + 1] = temp;
            j--;
        }
    }
    for(i = 0; i < number; i++) {
        printf("%d\n", array[i]);
    }
    return 0;
}
