// procedure MERGE-SORT(A, p, r)
//     if p < r
//     then q ← ,(p + r)/2-
//         MERGE-SORT(A, p, q)
//         MERGE-SORT(A, q + 1, r)
//         MERGE(A, p, q, r)


// procedure MERGE(A, p, q, r)
//     n1 ← q − p + 1; n2 ← r − q
//     allocate arrays L[1 ...n1 + 1] and R[1 ...n2 + 1]
//     for i ← 1 to n1
//         do L[i] ← A[p + i − 1]
//     for j ← 1 to n2
//         do R[j] ← A[q + j]
//     L[n1 + 1] ← ∞; R[n2 + 1] ← ∞
//     i ← 1; j ← 1
//     for k ← p to r
//         do if L[i] ≤ R[j]
//             then A[k] ← L[i]
//                 i ← i + 1
//             else A[k] ← R[j]
//                 j ← j + 1
