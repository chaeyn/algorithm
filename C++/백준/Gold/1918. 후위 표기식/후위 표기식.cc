#include <bits/stdc++.h>
using namespace std;

int precedence(string op) {
    if (op == "(" or op == ")") return 0;
    if (op == "+" or op == "-") return 1;
    if (op == "*" or op == "/") return 2;
    return -1;
}

vector<string> infix_to_postfix(vector<string>& expr) {
    stack<string> stk;
    vector<string> output;

    for (const auto& term : expr) {
        if (term == "(") {
            stk.push(term);
        } else if (term == ")") {
            while (!stk.empty()) {
                string op = stk.top();
                stk.pop();
                if (op == "(") {
                    break;
                }
                output.push_back(op);
            }
        }
        else if (term == "+" || term == "-" || term == "*" || term == "/") {
            while (!stk.empty()) {
                string op = stk.top();
                if (precedence(term) <= precedence(op)) {
                    output.push_back(op);
                    stk.pop();
                } else break;
            }
            stk.push(term);
        }
        else output.push_back(term);
    }
    while (!stk.empty()) {
        string op = stk.top();
        output.push_back(op);
        stk.pop();
    }
    return output;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string infix;
    cin >> infix;

    vector<string> v;
    for (int i=0; i<infix.length(); i++) {
        v.push_back(string(1, infix[i]));
    }

    vector<string> res = infix_to_postfix(v);

    for (const auto& term : res) {
        cout << term;
    }

    return 0;
}
