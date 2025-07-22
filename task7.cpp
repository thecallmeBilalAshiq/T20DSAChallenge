#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> grid[i][j];

    int maxSum = INT_MIN;

    // Try every center
    for (int cx = 0; cx < n; cx++) {
        for (int cy = 0; cy < n; cy++) {
            int currSum = 0;

            for (int r = 0; ; r++) {
                bool inBounds = true;

                // Check boundary of the diamond
                if (cx - r < 0 || cx + r >= n || cy - r < 0 || cy + r >= n)
                    break;

                // Add only the new ring at radius r
                for (int dx = -r; dx <= r; dx++) {
                    int x = cx + dx;
                    int dy = r - abs(dx);

                    if (cy - dy >= 0 && cy - dy < n)
                        currSum += grid[x][cy - dy];
                    if (dy != 0 && cy + dy >= 0 && cy + dy < n)
                        currSum += grid[x][cy + dy];
                }

                maxSum = max(maxSum, currSum);
            }
        }
    }

    cout << maxSum << "\n";
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> grid(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> grid[i][j];

    int maxSum = INT_MIN;

    // Try every center
    for (int cx = 0; cx < n; cx++) {
        for (int cy = 0; cy < n; cy++) {
            int currSum = 0;

            for (int r = 0; ; r++) {
                bool inBounds = true;

                // Check boundary of the diamond
                if (cx - r < 0 || cx + r >= n || cy - r < 0 || cy + r >= n)
                    break;

                // Add only the new ring at radius r
                for (int dx = -r; dx <= r; dx++) {
                    int x = cx + dx;
                    int dy = r - abs(dx);

                    if (cy - dy >= 0 && cy - dy < n)
                        currSum += grid[x][cy - dy];
                    if (dy != 0 && cy + dy >= 0 && cy + dy < n)
                        currSum += grid[x][cy + dy];
                }

                maxSum = max(maxSum, currSum);
            }
        }
    }

    cout << maxSum << "\n";
    return 0;
}
