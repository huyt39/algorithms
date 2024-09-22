#include <iostream>
using namespace std;

int main(){

int n;
cin>>n;
long s = 0;
unsigned int arr[n];

for (int i = 0; i < n; i++){
    cin>>arr[i];
    s += arr[i];
}
cout<<s;
return 0;
}