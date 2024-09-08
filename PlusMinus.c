#include<stdio.h>
int main(){
    int arr[100], n;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    float pos=0;
    float neg=0;
    float zero=0;
    for(int i=0;i<n;i++){
        if (arr[i]>0) pos++;
        if (arr[i]<0) neg++;
        if(arr[i]==0) zero++;
    }
    printf("%.6f\n",pos/n);
    printf("%.6f\n",neg/n);
    printf("%.6f\n",zero/n);
    return 0;
}