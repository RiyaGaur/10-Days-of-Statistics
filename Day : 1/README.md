# 1.Quartiles

<h2>Objective</h2>
In this challenge, we practice calculating quartiles.

<h2>Task</h2>
Given an array, X , of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1,Q2, and Q3 are integers.

<h2>Input Format</h2>

The first line contains an integer, n , denoting the number of elements in the array.
The second line contains n space-separated integers describing the array's elements.

<h2>Constraints</h2>
<ul>
		<li>5<=n<=50</li>
		<li> -1<=xi<=100, where xi is the ith element of the array X.</li>
</ul>

<h2>Output Format</h2>

Print 3 lines of output in the following order:

The first line should be the value of Q1.
The second line should be the value of Q2.
The third line should be the value of Q3.

# 2.Interquartile Range

<h2>Objective</h2>
In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

<h2>Task</h2>
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e.,Q3-Q1 ).

Given an array, X , of n integers and an array, F , representing the respective frequencies of X's elements, construct a data set, S , where each xi occurs at frequency fi. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e.,12.3 format).

<strong>Tip</strong>: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.

<h2>Input Format</h2>

The first line contains an integer, n , denoting the number of elements in arrays X and F.
The second line contains n space-separated integers describing the respective elements of array X.
The third line contains n space-separated integers describing the respective elements of array X.

<h2>Constraints</h2>
<ul>
	<li> 5<=n<=50</li>
	<li> -1<=xi<=100, where  is the  element of array X.</li>
	<li> -1<=summation of fi from i=0 to n-1 <=10^3, where fi is the ith element of array F.</li>
	<li>The number of elements in D is equal to summation F .</li>
</ul>

<h2>Output Format</h2>

Print the interquartile range for the expanded data set on a new line. Round your answer to a scale of 1 decimal place (i.e., 12.3 format).

# 3.Standard Deviation

<h2>Objective</h2>
In this challenge, we practice calculating standard deviation.

<h2>Task</h2>
Given an array, X , of N integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e.,12.3  format). An error margin of +-0.1 will be tolerated for the standard deviation.

<h2>Input Format</h2>

The first line contains an integer,N , denoting the number of elements in the array.
The second line contains N space-separated integers describing the respective elements of the array.

<h2>Constraints</h2>
<ul>
	<li> 5<=N<=100</li>
	<li> -1<=xi<=10^5, where xi is the ith element of array X.</li>
</ul>

<h2>Output Format</h2>

Print the standard deviation on a new line, rounded to a scale of 1 decimal place (i.e.,12.3 format).
