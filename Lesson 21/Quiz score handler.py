scores=[15,18,20,35,47,52,60,72]
n, target=len(scores),60
print("=== quiz score finder (n=",n, "scores)===")
print("Scores:", scores,"|Target:", target)
print()

steps=0
for i in range(n):
    steps+=1
    if scores[i]==target:
        print("Linear search: index=",i , "|steps=", steps, "|o(n)")
        break
print()

lo, hi, steps=0, n-1, 0
while lo<=hi:
    mid=(lo+hi)//2
    steps+=1
    if scores[mid]==target:
        print("Binary search: inedx=",mid, "|steps=", steps, "|O(log n)")
        break
    elif scores[mid]<target:
        lo=mid+1
    else:
        hi=mid-1
print()

def binary_search_rec(scores, lo, hi, target, calls=0):
    calls+=1
    if lo>hi:
        return -1, calls
    mid=(lo+hi)//2
    if scores[mid]==target:
        return mid, calls
    elif scores[mid]<target:
        return binary_search_rec(scores, mid+1, target, calls)
    else:
        return binary_search_rec(scores, mid-1, target, calls)


print("=== Space and Complexity Summary ===")
print("Iterative : O(1) space  — only lo, hi, mid")
print("Recursive : O(log n) space —", calls, "stack frames for n =", n)
print()
print("Complexity ladder (n =", n, "):")
print("O(1)     : 1 step   — constant, never grows")
print("O(log n) :", steps, "steps  — halving, grows slowly")
print("O(n)     :", n, "steps  — linear, grows with n")
print("O(n^2)   :", n * n, "steps — quadratic, grows fast!")

