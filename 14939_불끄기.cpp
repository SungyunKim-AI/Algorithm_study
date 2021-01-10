#include<iostream>
#include <string>
using namespace std;

int mSwitch[10];
int mCheck[10];

void switchOnOff(int row, int col) {
    mCheck[row] ^= (1 << (10 - col - 1));

    if (row) {
        mCheck[row - 1] ^= (1 << (10 - col - 1));
    }
    
    if (row != 9) {
        mCheck[row + 1] ^= (1 << (10 - col - 1));
    }

    if (col) {
        mCheck[row] ^= (1 << (10 - col));
    }

    if (col != 9) {
        mCheck[row] ^= (1 << (10 - col - 2));
    }
}


int main() {

    for (int i = 0; i < 10; i++) {
        string input;
        cin >> input;

        for (int j = 0; j < 10; j++) {
            if (input[j] == 'O') { mSwitch[i] |= (1 << j); }
        }
    }

    int result = 101;
    for (int candidate = (1 << 10) - 1; candidate >= 0; candidate--)
    {
        int count = 0;
        for (int i = 0; i < 10; i++)
        {
            mCheck[i] = mSwitch[i];
        }
        
        for(int col = 1; x < 10; x++)
        
    }
    


}
