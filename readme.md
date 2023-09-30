## Installation

To install the required libraries, run the following command in your terminal:

```shell
pip install -r requirements.txt
```

# Performance Comparison Script Overview

This script compares various Python methods in terms of execution time, memory usage, and CPU usage.

## Script Sections

### 1. **Method Definitions:**
   Defines various Python methods to be compared, such as using loops, list comprehensions, map function, and numpy, including a recursive function.

### 2. **Methods Dictionary:**
   Holds references to the method functions and a flag indicating whether the method is recursive.

```python
methods = {
    'For Loop': {'func': for_loop, 'recursive': False},
    # ... other methods ...
}
```

### 3. **Performance Analysis Loop:**

    Iterates over different sample sizes and repeat counts.
    Runs each method and measures execution time, memory usage, and average CPU usage.
    Skips recursive methods if the sample size exceeds the adjusted system recursion limit.

### 4. **Result Compilation:**

    For each sample size, it creates a summary table, sorts it by execution time, and stores its string representation.

### 5. **Result Output:**

    After all computations, prints out each summary table, one for each sample size.

Usage:
```
python performance_comparison.py
```

