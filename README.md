# Levenshtein-Distance

Algorithm [Levenshtein distance](https://people.cs.pitt.edu/~kirk/cs1501/Pruhs/Spring2006/assignments/editdistance/Levenshtein%20Distance.htm) or edit the distance between two "strings"
(two chains) the minimum number of operations required to transform one chain into another. 

By "operations" we mean the insertion, exclusion or substitution of a character. Used for applications that need to determine how two strings are similar, as is the case with spell checkers.

```python
    print("Levenshtien distance: {0}%" .format(compare("Kleyto", "Kleyton")))
```
