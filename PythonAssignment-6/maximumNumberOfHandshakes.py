'''The program calculates the total number of handshakes that occur when each student in a classroom shakes hands with every other student exactly once. The scenario is set in a classroom where Raj's teacher, Anu, assigns this activity on Raj's first day at school.

Logical Approach:

Read Input:
Read the number of students N in the classroom as an integer.

Calculate Total Handshakes:
To calculate the total number of handshakes, use the formula (N×(N−1))/2. This formula calculates the number of unique pairs that can be formed from N students, as each handshake involves a pair of students.
Here, N * (N - 1) gives the total number of handshakes if every student shakes hands with every other student, including repetitions. Dividing by 2 removes these repetitions, ensuring each pair is only counted once.

Output:
Print the total number of handshakes.

Example for Clarity:

If N is 5:
The 1st student shakes hands with 4 other students.
The 2nd student shakes hands with 3 other students (excluding the 1st).
The 3rd student shakes hands with 2 other students (excluding the 1st and 2nd).
The 4th student shakes hands with 1 other student (excluding the 1st, 2nd, and 3rd).
The 5th student doesn't shake hands as they have already shaken hands with everyone.
The total handshakes are 4 + 3 + 2 + 1 = 10.
So, the output will be 10.

If N is 3:
The 1st student shakes hands with 2 other students.
The 2nd student shakes hands with 1 other student (excluding the 1st).
The 3rd student doesn't shake hands as they have already shaken hands with everyone.
The total handshakes are 2 + 1 = 3.
So, the output will be 3.'''


n=int(input())

res = (n*(n-1))//2
print(res)