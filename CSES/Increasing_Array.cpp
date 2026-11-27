#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<long long> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long count = 0;
    for (int i = 1; i < n; i++) {
        if (arr[i - 1] > arr[i]) {
            count += (arr[i - 1] - arr[i]);
            arr[i] = arr[i - 1];
        }
    }

    cout << count << "\n";
    return 0;
}
