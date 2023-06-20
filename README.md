# ReprTraceback

ReprTraceback is a module that utilizes the `sys.excepthook` to throw custom traceback messages. Specifically, it includes values of positional, var, and keyword arguments.

## Before & After
Before
```python
Traceback (most recent call last):
  File "main.py", line 17, in <module>
    main()
  File "main.py", line 13, in main
    get_element(n, verbose, *args, **kwargs)
  File "main.py", line 5, in get_element
    return my_list[k]
           ~~~~~~~^^^
IndexError: list index out of range
# What is k? What was passed in? We'll never know. Hopefully it's easy to reproduce.
```

After
```python
Traceback (most recent call last):
  File "main.py", line 17, in <module>
    main()
  File "main.py", line 13, in main
    main()
         ^^
  File "main.py", line 5, in get_element
    get_element(k=5, verbose=True, args=('my', 'var', 'args'), kwargs={'Repr': 'Traceback'})
                ^^^^^^^^^^
IndexError: list index out of range
```


## Installation
You can install the project using `pip`:

```shell
pip install ReprTraceback
```


## Usage
Import and Init ReprTraceback.
```python
from ReprTraceback import ReprTraceback

# Call the init() function to set up the new traceback handler
ReprTraceback.init()

# ...
# Your code here
# ...

# When an exception occurs, the traceback will include the actual argument values
# passed to functions, providing better insight into the code flow and bug diagnosis.
```
