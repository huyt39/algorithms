#include <stdio.h>
int main(){
    int n;
    scanf ("%d",&n);
    int a[n];
    for (int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    int k,x;
    scanf ("%d %d",&k,&x);
    for(int i=n;i>k+1;i--){
        a[i]=a[i-1];
    }
    a[k]=x;
    for(int i=0;i<=n;i++){
        printf("%d ",a[i]);
    }
    return 0;
}