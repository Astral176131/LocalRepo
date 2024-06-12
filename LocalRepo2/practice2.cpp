#include<bits/stdc++.h>
using namespace std;

int palin(string arr,int n)
{
    int z=n%2;
    int y=n-1;
    for(int i=0;i<z;i++)
    {
        if(arr[i]!=arr[y])
            return 0;
        y--;
    }
    return 1;
}

int main()
{
    string arr;
    cout<<"Enter the string: "<<endl;
    cin>>arr;
    int a=palin(arr,arr.size());
    if(a==1)
        cout<<"The entered string "<<arr<<" is a palindrome[1=Yes/0=No]: "<<a<<endl;
    else
        cout<<"The entered string is not a palinrome [1=Yes/0=No]: "<<a<<endl;
    
}