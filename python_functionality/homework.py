from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
<<<<<<< HEAD
    return [{'name': i['name'].capitalize(), 'age': i['age']} if i.get('name')
            else {'age': i['age']} for i in data]
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
<<<<<<< HEAD
    return [{k: v for k, v in d.items() if k not in redundant_keys}
            for d in data]
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
<<<<<<< HEAD
    return [i for i in data if {v for v in i.values() if v == value}]
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
<<<<<<< HEAD
    return min(data) if data else None
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
<<<<<<< HEAD
    return min([str(i) for i in data], key=len) if data else None
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
<<<<<<< HEAD
    return min([i for i in data if i.get(key)], key=lambda x: x[key])
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
<<<<<<< HEAD
    return max([i for l in data for i in l])
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
<<<<<<< HEAD
    return sum([i for i in data])
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
<<<<<<< HEAD
    return sum([ord(i) for i in text])
=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
<<<<<<< HEAD
    for i in range(2, 201):
        for n in range(2, i):
            if i%n == 0:
                break
        else:
            yield i

=======
    pass
>>>>>>> 6ef23a9a9c2f17460a24c9336a33cfea7d523ad0
