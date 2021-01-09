#include<iostream>
#include <string>
using namespace std;

int mSwitch[10][10] = {0, };

int main() {

    for (int i = 0; i < 10; i++) {
        string input;
        cin >> input;

        for (int j = 0; j < 10; j++) {
            if (input[j] == 'O') { mSwitch[i][j] = 1; }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            cout << mSwitch[i][j];
        }
        cout << endl;
        
    }
    
    
    

}
