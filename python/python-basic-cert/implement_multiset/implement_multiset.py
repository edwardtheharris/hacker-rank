#!/usr/bin/env python3
"""This module implements a Multiset data structure."""

import os

class Multiset:
    """This class implements a multiset."""

    multiset = []

    def add(self, val):
        """Add one occurrence of val from the multiset, if any."""
        self.multiset.append(val)
        return self.multiset

    def remove(self, val):
        """Removes one occurrence of val from the multiset, if any."""
        ret_val = self.multiset
        if self.multiset.count(val) == 0:
            pass
        else:
            v_index = self.multiset.index(val)
            del self.multiset[v_index]
        return ret_val

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        ret_val = False
        if val in self.multiset:
            ret_val = True
        return ret_val

    def __len__(self):
        # returns the number of elements in the multiset
        ret_val = len(self.multiset)
        return ret_val


if __name__ == '__main__':
    def perform_operations(ops_list):
        """Perform operations with the multiset."""
        m = Multiset()
        ret_value = []
        for op_str in ops_list:
            elems = op_str.split()
            if elems[0] == 'size':
                ret_value.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    ret_value.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return ret_value

    q = int(input())
    operations = []
    for _ in range(q):
        operations.append(input())

    result = perform_operations(operations)

    with open(os.environ.get('OUTPUT_PATH'), 'w', encoding='utf-8') as fptr:
        fptr.write('\n'.join(map(str, result)))
        fptr.write('\n')
