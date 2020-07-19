#include <stdio.h>
#include <queue>

using namespace std;

int main(void) {
    queue<int> q;
    q.push(7);
    q.push(5);
    q.push(4);
    q.pop();
    q.push(6);
    while(!q.empty()) {
        cout << q.front() << ' ';
        q.pop();
    }
    return 0;
}
