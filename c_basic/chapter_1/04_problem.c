#include <stdio.h>

int main(){
// write the formula for the simple intrest
// prt/100
    int p,r,t;
    printf("enter the principle amount:\n");
    scanf("%d",&p);
    printf("enter the rate:\n");
    scanf("%d",&r);
    printf("Enter the time period:\n");
    scanf("%d",&t);
    printf("total simple intrest %d\n",(p*r*t)/100);
    return 0;
}
