#include<stdio.h>
#include<stdbool.h>
int main(){
    int n;
    scanf("%d",&n);
    int a[n][5];
    int count[100]={0};
    int unique[n*5];
    int unique_count=0;
    for (int i=0;i<n;i++){
        for(int j=0;j<5;j++){
            scanf("%d",&a[i][j]);
        }
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<5;j++){
            int num=a[i][j];
            if(num==-1){
                continue;
            }
            bool found=false;
            for(int m=0;m<unique_count;m++){
                if(unique[m]==num){
                    count[m]++;
                    found=true;
                    break;
                }
            }
        if(!found){
            unique[unique_count]=num;
            count[unique_count]=1;
            unique_count++;
        }   
        }
    }
int max_count=0;
for(int i=0;i<unique_count;i++){
    if(count[i]>max_count) max_count=count[i];
}
for(int i=0;i<unique_count;i++){
    if(count[i]==max_count){
        printf("%d ",unique[i]);
    }
}
return 0;
}