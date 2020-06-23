<h2>Objective</h2>
In this challenge, we practice calculating the mean, median, and mode. 

<h2>Task</h2>
Given an array,X, of N integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of 1 decimal place (i.e.,12.3, 7.0  format).

<h2>Input Format</h2>

The first line contains an integer, N , denoting the number of elements in the array.
The second line contains N space-separated integers describing the array's elements.

<h2>Constraints</h2>
<ul>
			<li>10<=N<=2500</li>
			<li>0<xi<=10^5, where xi is the ith element of the array.</li>
</ul>

<h2>Output Format</h2>

Print 3 lines of output in the following order:
<ol>
			<li>Print the mean on a new line, to a scale of 1 decimal place (i.e.,12.3 ,7.0 ).</li>
			<li>Print the median on a new line, to a scale of 1 decimal place (i.e.,12.3 ,7.0 ).</li>
			<li>Print the mode on a new line; if more than one such value exists, print the numerically smallest one.</li>
</ol>

<hr>
import math
import collections
n=int(input())
t=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=t[i]
    mode=sum/n
print(mode)
n = len(t) 
t.sort()
if n % 2 == 0: 
    median1 = t[n//2] 
    median2 = t[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = t[n//2] 
print(median)
occurrences = collections.Counter(t)
max = max(occurrences.keys(), key=(lambda k: occurrences[k]))
print(max)

