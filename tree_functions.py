import jmespath
from jmespath import functions
import itertools
import operator

class TreeFunctions(functions.Functions):

    @functions.signature({'types': ['array'], 'variadic': True})
    def _func_product(self, *arrays):
        return [list(x) for x in itertools.product(*arrays)]

    @functions.signature({'types': ['array'], 'variadic': True})
    def _func_zip(self, *arrays):
        return zip(*arrays)

    @functions.signature({'types': []})
    def _func_descent(self, root):

        def type_dispatch(node):
            actual_typename = type(node).__name__
            jp_typename = self._convert_to_jmespath_type(actual_typename)
            if jp_typename == 'object':
                return tree_walk(node, node.values())
            elif jp_typename == 'array':
                return tree_walk(node, node)
            else:
                return tree_walk(node, [])

        def tree_walk(node, children):
            yield node
            for child in children:
                for descendant in type_dispatch(child):
                    yield descendant

        return list(type_dispatch(root))
