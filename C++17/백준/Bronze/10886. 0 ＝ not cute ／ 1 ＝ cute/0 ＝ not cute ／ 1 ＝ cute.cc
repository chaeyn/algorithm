#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int positive_count = 0, negative_count = 0;

    for (int i = 0; i < n; i++)
    {
        int answer;
        cin >> answer;

        if (answer == 0)
        {
            negative_count++;
        }
        else if (answer == 1)
        {
            positive_count++;
        }
    }

    if (positive_count > negative_count)
    {
        cout << "Junhee is cute!";
    }
    else
    {
        cout << "Junhee is not cute!";
    }
    return 0;
}