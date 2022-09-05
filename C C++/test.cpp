#include <bits/stdc++.h>
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = a; i < b; i++)
#define iREP(i,a,b) for (int i = a; i > b; i--)

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll t, n, x, s;
    cin >> t;
   
    while (t > 0){
         map<int, int> m;
        t-=1;
        cin >> n;
        vi v;
        s = 0;
        REP(i, 0, n){
            cin>>x;
            v.PB(x);
        }
        iREP(i, n - 1, -1){
            if(m.count(v[i])){
                cout<<i + 1<<"\n";
                s=1;
                break;
            }
            else
                m.insert(pi(v[i], 1));
        }
        if(!s)
            cout<<0<<"\n";
    }

}