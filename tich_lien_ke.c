#include<stdio.h>
int Max(int mul, int max){
    if(mul>max) max=mul;
    return max;
}
int main(){
    int n;
    scanf ("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    int mul=1;
    int max=a[0]*a[1];
    for(int i=1;i<n-1;i++){
        mul=a[i]*a[i+1];
        max=Max(mul,max);
    }
    printf("%d",max);
    return 0;
}