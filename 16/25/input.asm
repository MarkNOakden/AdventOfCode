00:	cpy a d //d = a
01:	cpy 14 c

A:	

02:	cpy 182 b //d += 182

B:	

03:	inc d
04:	dec b
05:	jnz b -2 // B:

06:	dec c //14 times -- now d = initial_a + 14*182
07:	jnz c -5 // goto A:

	//code so far: d = initial_a + 14 * 182
X:
	
08:	cpy d a // a = d

Z:
	
09:	jnz 0 0 // noop ?
10:	cpy a b // b = a
11:	cpy 0 a // a = 0

W:
	
12:	cpy 2 c // c = 2

D:
	
13:	jnz b 2 // if b != 0 goto C:
14:	jnz 1 6 // goto E:

C:
	
15:	dec b // b -= 1
16:	dec c // c -= 1
17:	jnz c -4 // if c != 0 goto D:

18:	inc a // a += 1
19:	jnz 1 -7 // goto W:

E:
	
20:	cpy 2 b // b = 2

G:
	
21:	jnz c 2 // if c != 0 goto F:
22:	jnz 1 4 // goto H:

F:
	
23:	dec b
24:	dec c
25:	jnz 1 -4 // goto G:

H:
	
26:	jnz 0 0
27:	out b
28:	jnz a -19 // if a != 0 goto Z:
29:	jnz 1 -21 // goto X:
