#include <iostream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int tc;
    cin >> tc;  // Number of test cases

    while (tc--)
    {
        long long x, y;
        cin >> x >> y;

        // If x is smaller than y, then calculate based on y
        if (x < y)
        {
            // If y is odd
            if (y % 2 == 1)
            {
                long long r = y * y;  // Calculate y squared
                cout << r - x + 1 << "\n";  // Move from the top end of the column
            }
            // If y is even
            else
            {
                long long r = (y - 1) * (y - 1) + 1;  // Calculate (y-1) squared + 1
                cout << r + x - 1 << "\n";  // Move from the left end of the row
            }
        }
        // If y is smaller than or equal to x, then calculate based on x
        else
        {
            // If x is even
            if (x % 2 == 0)
            {
                long long r = x * x;  // Calculate x squared
                cout << r - y + 1 << "\n";  // Move from the right end of the row
            }
            // If x is odd
            else
            {
                long long r = (x - 1) * (x - 1) + 1;  // Calculate (x-1) squared + 1
                cout << r + y - 1 << "\n";  // Move from the bottom end of the column
            }
        }
    }
    return 0;
}
