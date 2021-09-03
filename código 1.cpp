#include <iostream> // todo comando, função, ou quaçquer outra coisa deve ser usada dentro do int main
using namespace std;
int main() {
    // Read and print three floating point numbers
    float a, b, c;
    cin >> a >> b >> c; // input
    // output
    cout << a << ", " << b << ", " << c << endl;
    
    cout <<"x-intercept: ";
    float p = -c/a;
    float s = b/a;
    if (a != 0){
        cout << "O produto é "<< p <<","<<"e a soma é "<< s << ", ";
    }
    else {
        cout<<"none, ";
    return 0;
}
}
