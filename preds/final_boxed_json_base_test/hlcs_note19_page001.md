```markdown
# C++ Tutorials

## Example 1

```cpp
#include <iostream>
using namespace std;

int main()
{
    double x = 1.2;
    int y = (int)x; // Explicit type casting
    cout << "Value of y = " << y;
    return 0;
}
```

## Example 2

```cpp
#include <iostream>
using namespace std;

int main()
{
    double x = 1.2;
    int y = static_cast<int>(x); // Using static_cast for explicit type casting
    cout << "Value of y = " << y;
    return 0;
}
```
```