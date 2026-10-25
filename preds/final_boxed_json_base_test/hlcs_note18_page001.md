```markdown
# C++ Tutorials

## Implicit Type Casting
```cpp
#include <iostream>
using namespace std;
int main()
{
    short x = 20;
    int y = x; // implicit type casting
    cout << "The value of x" << x << endl;
    cout << "The value of y" << y;
    return 0;
}
```

## Explicit Type Casting
Explicit type casting occurs when the user manually changes data from one type to another. This is known as explicit type casting.

### Syntax
```cpp
(data_type) expression;
```

### Examples
- long double -> double -> float -> long int -> unsigned int -> int -> short int -> char
```