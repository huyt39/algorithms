#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    int cnt1=0,cnt2=0;
    for(int i=0;i<n-1;i++){
        if(a[i]<=a[i+1]) cnt1++;
        else cnt1=0;
    }
    for(int i=0;i<n-1;i++){
        if(a[i]>=a[i+1]) cnt2++;
        else cnt2=0;
    }
    if(cnt1==n-1 || cnt2==n-1) printf ("YES");
    else printf ("NO");
    return 0;
}