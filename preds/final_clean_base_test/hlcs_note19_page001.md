```markdown
# C++ Tutorials

## Example 19

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

## Additional Notes

- **Type Casting**: Converting one data type to another explicitly.
- **Example Code Explanation**:
  - `double x = 1.2;` declares a variable `x` of type `double` and assigns it the value `1.2`.
  - `(int)x` converts the `double` value `1.2` to an `int`, which results in `1` because the integer part is taken.
  - `cout << "Value of y = " << y;` outputs the value of `y` to the console.

## Diagrams

[Diagram: Flowchart of Type Casting]
```
```