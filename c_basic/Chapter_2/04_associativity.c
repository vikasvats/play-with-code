#include <stdio.h>

int main(){
    int a = 3;
    int b = 6;
    int c = 9;
    // there prcidence is a*b/c first multiply is happened
    //  then divide will happen
    printf("The value is %d \n", a*b/c + 7);
    // 3*b/2*c + 7*a
    //3*b/2*c + 21
    //3*6/2*c + 21
    // 18/2*c + 21
    // 9*c + 21
    // 9*9 +21
    // 81 + 21
    // 102
    printf("The value is %d \n", 3*b/2*c +7*a);
    return 0;
}
