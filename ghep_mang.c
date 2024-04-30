#include <stdio.h>
void sort (int a[], int n){
    int temp;
    for(int i=0; i<n-1; i++){
        for (int j=i+1; j<n; j++){
            if (a[i]>a[j]){
                temp=a[j];
                a[j]=a[i];
                a[i]=temp;
            }
        }
    }
}
int main(){
    int n, m;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    scanf ("%d",&m);
    int b[m];
    for(int i=0;i<m;i++){
        scanf("%d",&b[i]);
    }
    int k=m+n;
    int c[k];
    for(int i=0;i<n;i++){
        c[i]=a[i];
    }
    for (int j=0;j<m;j++){
        c[j+n]=b[j];
    }
    sort(c,k);
    for(int i=0;i<k;i++){
        printf ("%d ", c[i]);
    }
    return 0;
}