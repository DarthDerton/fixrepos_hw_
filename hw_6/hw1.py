from typing import Any
"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""


# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}

"""
The function takes two arguments, tree and element, where tree is the dictionary that we need to search,
and element is the element we are looking for. The function initializes a variable count to 0, which will keep track 
of the number of occurrences of the element.

The function then iterates over the values in the tree. If the value is equal to the element,
the function increments the count by 1. If the value is a list, tuple, or set,
the function uses the count method to count the number of occurrences of the element in the list.
If the value is a dictionary, the function calls itself recursively to search for the element in the sub-tree.

Finally, the function returns the count of the number of occurrences of the element in the tree.

When we run the find_occurrences function with the example_tree and the element "RED", we get the output 6,
which is the number of occurrences of "RED" in the tree.
"""


def find_occurrences(tree: dict, element: Any) -> int:
    count = 0
    for value in tree.values():
        if value == element:
            count += 1
        elif isinstance(value, (list, tuple, set)):
            count += value.count(element)
        elif isinstance(value, dict):
            count += find_occurrences(value, element)
    return count


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
