#include <iostream>
#include <math.h>
using namespace std;

int n_fatores(int n){
    int fatores = 0;
    int c = 0;
    for(int i = 2; i < sqrt(n); i++){
        while(n % i == 0){
            if(c == 0){
                fatores += 1;
                c += 1;
            }
            n = n / i;
        }
        c = 0;
    }
    if(n != 1){
        //cout << n << endl;
        fatores += 1;
    }
    return fatores;
}

int main() {
    int Num1; 
    cin >> Num1;
    cout << Num1 << " " <<  n_fatores(Num1);
    return 0;
}