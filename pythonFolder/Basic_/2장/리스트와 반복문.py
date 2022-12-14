for i, e in enumerate(['a','b']):
  print("i = %d, e = %s" % (i, e));
#enumerate 명령은 리스트의 원소를 반복하면서 동시에 인덱스 값도 생성한다.

s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a1 = [90, 85, 95, 80, 90, 100, 85, 75, 85, 80]
a2 = [95, 90, 90, 90, 95, 100, 90, 80, 95, 90]
# for i, (a1i, a2i) in enumerate(zip(a1, a2)):
#     s[i] = a1i + a2i
#     print(s[i]);

    #zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환

#Zip 함수

what = []
a12 = list(zip(a1, a2));
print(a12)
#이 때 소괄호로 표시된 묶음은 튜플(tuple)이라고 하며 리스트와 사용법이 거의 동일하다. 따라서 모든 학생의 두 과목 성적 합산을 구하는 코드는 다음과 같이 고칠 수 있다.
for a1i, a2i in zip(a1,a2):
  what.append(a1i + a2i);
  print(what)

  #연습문제
x = [
  ["길동", 90],
  ["철수", 80],
  ["영수", 70],
  ["방자", 60],
]

x1,x2,x3,x4 = x;
y = list(zip(x1,x2,x3,x4))[0];
print(y)

#x앞의 *은 뭘까.. x를 자동적으로 루프돌게 하는거같기는 한데..
z1= list(zip(*x))[0]
print(z1)
print("%s의 %s 과목 점수는 %d점이다." % ("철수", "수학", 100));