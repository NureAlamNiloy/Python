#include <bits/stdc++.h>
using namespace std;

int main(){

    long long  n,count = 0;
    cin >> n;
    vector<int>arr(n);
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    } 
    for (int j = 0; j < n; j++){
        for (int i = 0; i < n-1; i++){
            if (arr[i] > arr[i+1]){
                int tamp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = tamp;
                count ++;
            } 
        }
    } 
    cout << count << endl;
    
    return 0;
}