#include<stdio.h>
int isPrime(int k){
    if(k<=1) return 0;
    else{
        for(int i=2;i<k;i++){
            if(k%i!=0) printf("%d ",k);
        }
    }
}
int main(){
    int n;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++){
        isPrime(a[i]);
    }
}