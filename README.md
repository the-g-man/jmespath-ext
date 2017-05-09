# jmespath-ext
New functions for JMESPath

# Functions

## product

    list product([list *argument, [, list $...]])
    
A variadic function taking one or more lists as arguments which returns the Cartesian product of those lists.
    
### Example

| **Expression** | ``product( `["a", "b"]`, `["c", "d"]`)`` |
| **Gives**  |`[ ["a", "c"], ["a", "d"], ["b", "c"], ["b", "d"] ]` |
