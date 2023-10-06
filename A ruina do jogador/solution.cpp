#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define endl "\n"
#define optimize ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)


using namespace std;
using namespace __gnu_pbds;

int main() {
    int EV1, EV2, AT, D;

    while (true) {
        optimize;
        cin >> EV1 >> EV2 >> AT >> D;

        if (EV1 == 0 && EV2 == 0 && AT == 0 && D == 0) {
            break;
        }

        EV1 = ceil(static_cast<double>(EV1) / D);
        EV2 = ceil(static_cast<double>(EV2) / D);
        int n = EV1 + EV2;

        double x, y;

        if (AT == 3) {
            x = static_cast<double>(EV1);
            y = static_cast<double>(n);
        } else {
            x = 1 - pow((6 - AT) / static_cast<double>(AT), static_cast<double>(EV1));
            y = 1 - pow((6 - AT) / static_cast<double>(AT), static_cast<double>(n));
        }

        double resposta = round(100 * x / y * 10) / 10.0;
        cout << fixed << setprecision(1) << resposta << endl;
    }

    return 0;
}