#include <stdio.h>

int main(){
// write the formula to change the calcius to farenheight
    float c,f;
    printf("Enter you tempreatur in celcius");
    scanf("%f",&c);
    f = (c*9/5)+32;
    printf("temprature in farenheit is %f \n", f);
    return 0;
}
