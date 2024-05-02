#include<stdio.h>
int main(){
    int n;
    scanf ("%d",&n);
    int nn=n*10+n;
    int nnn=100*n+nn;
    int sum=n+nn+nnn;
    printf("%d",sum);
    return 0;
}