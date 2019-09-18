# # Fig 1.6 Algorithm for "query x and y"; the intersection of two postings lists p1 and p2.
# def INTERSECT(p1, p2):
#     answer←⟨⟩
#        while p1 ̸= NIL and p2 ̸= NIL
#            if docID(p1) = docID(p2):
#                 ADD(answer, docID(p1))
#                 p1 ← next(p1)
#                 p2 ← next(p2)
#             if docID(p1) < docID(p2):
#                 p1 ← next(p1)
#             if docID(p1) > docID(p2):
#                 p2 ← next(p2)
#             return answer


# # Ex1.10 Algorithm for "query x or y"; The merge of two postings lists list1 and list2.
# # Ia: answer is union of parts of p1 and p2 that has been go throught so far
# def UNION(p1, p2):
#     answer = set([docID(p1), docID(p2)])   # Ia established

#     while p1 != NIL or p2 != NIL:
#         if p1 == NIL and p2 != NIL:
#             ADD(answer, docID(p2))
#             p2 ← next(p2)

#         if p1 != NIL and p2 == NIL:
#             ADD(answer, docID(p1))
#             p1 ← next(p1)

#         if docID(p1) == docID(p2):
#             ADD(answer, docID(p1))
#             p1 ← next(p1)
#             p2 ← next(p2)

#         if docID(p1) != docID(p2):
#             ADD(answer, docID(p1))
#             ADD(answer, docID(p2))
#             p1 ← next(p1)
#             p2 ← next(p2)

#         # Ia re-established

#     # now answer is union of list1 and list2
#     return answer


# Ex1.11 Algorithm for "query x AND NOT y"
# Precond: l1[0..I), l2[0..J) are ascending lists of DocIDs, the posting list of x and y
# PostCond: answer is a list of elements in l1[0..I) AND NOT in l2[0..J);
# Invariant Inv(i,j): { answer is a list of elements in l1[0..i) AND NOT in l2[0..j) | 0<=i<=I, 0<=j<=J }
def conjunction_negation(l1, l2):

    I, J = len(l1), len(l2)

    answer, i, j = [], 0, 0  # Inv(0, 0) established as vacuous truth

    while i != I:

        if j == J:              # {l1[i] > Max(l2)} => l1[i] not in l2
            answer.append(l1[i])
            i = i + 1

            # Inv(i, j) re-established
            continue

        if l1[i] > l2[j]:       # 1. l1[i] can be in l2: keep checking
            j = j + 1

        elif l1[i] == l2[j]:      # 2. l1[i] in l2: skip it
            i, j = i+1, j+1

        elif l1[i] < l2[j]:       # 3. l1[i] not in l2: record it
            answer.append(l1[i])
            i = i + 1
        # Inv(i, j) re-established

    # Deduction: On the status here:
    # { j != J } And { l1[0..I), l2[0..J) are ascending }
    #   => {l1[I-1] < l2[j]}
    #   => l2[j] > max(l1) }
    #   => { l1[i] not in l2[j..J) | i in [0..N] }
    # Inv(I, j) AND { j != J }   =>   Inv(I, J)

    # Thus I(I, J) stands:
    #   answer is a list of elements in l1[0..I) AND NOT in l2[0..J)

    return answer


if __name__ == '__main__':
    l1 = [1, 3, 4, 5, 6, 8]
    l2 = [1, 2, 7, 8]
    l3 = [0]
    l4 = [9, 11, 32]

    assert conjunction_negation(l1, l3) == [1, 3, 4, 5, 6, 8]
    assert conjunction_negation(l1, l2) == [3, 4, 5, 6]
    assert conjunction_negation(l2, l1) == [2, 7]
    assert conjunction_negation(l4, l1) == [9, 11, 32]
    assert conjunction_negation(l2, l3) == [1, 2, 7, 8]
    assert conjunction_negation(l2, l2) == []
