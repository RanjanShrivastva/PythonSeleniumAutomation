"""
MRO = Method resolution Order
It works based on C3 Algorithm
C3 coined by Samuele Patroni
C3 follows DLR : Depth first, left to right
Algorithm
MRO(X) = X + Merge(MRO(P1), MRO(P2),....., Parent List
Head Element Vs Tail Terminology
Assume C1,C2,C3,C4
in the list: C1C2C3C4..
First Element is considered as Head as C1 and remaining will be considered as Tails as C2C3C4
Head: C1
Tail part: C2C3C4...
Functionality of merge
    1. take head of first list
    2. If the head is not in the tail part in any other list then add this head in result and remove it form all list
    3. If Head is present in tail part of any other list then , considered head element of the next
    list and continue the process
    
Note:
    child will get more priority
    If multiple parents are then left parent will get priority than right parent

"""