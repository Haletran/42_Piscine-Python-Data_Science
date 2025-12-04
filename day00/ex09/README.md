# ft_package

A tiny Python package with one function: `count_in_list`.

## Installation

Build and install locally:

```bash
make install
```

## Usage

```python
from ft_package import count_in_list

nums = [1, 2, 3, 2, 2]
print(count_in_list(nums, 2))  # Output: 3
```

## Function

```python
def count_in_list(array: list, searched: str) -> int:
    return array.count(searched)
```

Counts how many times `searched` appears in `array`.

## License

MIT
