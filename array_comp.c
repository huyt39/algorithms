#include<stdio.h>
#include<string.h>  
int main(){
    int n;
    scanf("%d",&n);
    int a[n],b[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++){
        scanf("%d",&b[i]);
    }
    int cnt=0;
    for(int i=0;i<n;i++){
        if(a[i]!=b[i]){
            cnt++;
        }
    }
    char comp[10];
    if(cnt>2) strcpy(comp, "false");
    else strcpy(comp, "true");
    printf("%s",comp);
    return 0;
}