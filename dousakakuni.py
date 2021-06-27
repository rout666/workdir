T=int(input())
for _ in range(T):
    S=input().split()
    S[2]=str(int(S[2])+1)
    print(" ".join(S))