#  다른 모든 지원자와 비교했을 때 
#  서류심사 성적과 면접시험 성적 중 
#  적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
#  즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 
#  서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.

# 지원자가 모두 한 장소에 모였다고 생각해 볼게요.

# 그 중에 한 지원자의 입장이 되어, 다른 지원자들의 면접, 서류 점수를 봅니다.

# 그 중에 어떤 한 사람이라도 나보다 두 점수가 더 높으면, 나는 선발이 안 됩니다.

# 그런 사람이 없으면 나는 선발되는 거고요.

# 이를 모든 지원자에 대해 다 해보는 것입니다.

from sys import stdin

a = [[],[]]
b = []

t = int(stdin.readline())
for i in range(0, t):
    n = int(stdin.readline())
    for j in range(0,n):
        x, y = list(map(int, stdin.readline().split()))
        a.append(x)
        b.append(y)

print(a)
print(b)