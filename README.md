# jmespath-ext
New functions for JMESPath for handling normalized, parallel or recursive data structures.

# Functions

## product

    list product([list *argument, [, list $...]])
    
A variadic function taking one or more lists as arguments which returns the Cartesian product of those lists - i.e. all possible lists where the 1st element is taken from the 1st input list, the 2nd input is taken from the 2nd input list, and so on.

The specification does not require any particular ordering of the output list.
    
| Example |     |
| ------- | --- |
| Expression | ``product( `["a", "b"]`, `["c", "d"]`)`` |
| Gives  |`[ ["a", "c"], ["a", "d"], ["b", "c"], ["b", "d"] ]` |

## zip

    list zip([list *argument, [, list $...]])
    
A variadic function taking one or more lists as arguments. It returns the zip of those lists - i.e. a list of lists, where the 1st element is a list of the 1st elements of each of the input lists, the 2nd element is a list of 2nd elements, and so on. The output list has the same length as the shortest input list.
    
| Example |     |
| ------- | --- |
| Expression | ``zip( `["a", "b"]`, `["c", "d"]`, `["e", "f", "g"]`)`` |
| Gives  |`[ ["a", "c", "e"], ["b", "d", "f"] ]` |

## descent

    list descent(any argument)
    
The `descent` function returns a list of all descendant nodes (children, grandchildren etc) of an input node (including the node itself).

No rigid ordering is required of an implementation but a parent must always precede any of its children in the output list. Therefore the first node of the output list is always required to be the input node itself.

| Example |     |
| ------- | --- |
| Expression | ``descent( `{"a": [1, 2], "b": {"c": 3, "d": 4}`)`` |
| Gives  |`[ {"a": [1, 2], "b": {"c": 3, "d": 4}, [1, 2], 1, 2, {"c": 3, "d": 4}, 3, 4 ]` |
