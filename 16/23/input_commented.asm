a = 12

00:	cpy a b		// b = a

01:	dec b		// b -= 1
02:	cpy a d		// d = a
03:	cpy 0 a		// a = 0

// 04..09 a = b * d
04:	cpy b c		// c = b

// 05..07  a += c
05:	inc a		// a += 1
06:	dec c		// c -= 1
07:	jnz c -2	// if c != 0 goto 05
	
08:	dec d		// d -= 1
09:	jnz d -5	// if d != 0 goto 04

10:	dec b		// b -= 1
11:	cpy b c		// c = b

// 12..15 c = 2 * c
12:	cpy c d		// d = c

// 13..15 c += d
13:	dec d		// d -= 1
14:	inc c		// c += 1
15:	jnz d -2	// if d != 0 goto 13
	
16:	tgl c		// toggle @ c
17:	cpy -16 c	// c = -16
18:	jnz 1 c		// goto 02

	------------------------------------------------------------
19:	cpy 85 c	// c = 85
20:	jnz 76 d	// goto 20 + d
21:	inc a
22:	inc d
23:	jnz d -2
24:	inc c
25:	jnz c -5

	------------------------------------------------------------
// once toggled: a += 76 * 85
19:	cpy 85 c	// c = 85
20:	cpy 76 d	// d = 76
	// 21..23 a += 76
21:	inc a
22:	dec d
23:	jnz d -2
	
24:	dec c
25:	jnz c -5
