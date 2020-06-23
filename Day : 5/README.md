# 1.Poisson Distribution I

<h2>Objective</h2>
In this challenge, we learn about Poisson distributions.

<h2>Task</h2>
A random variable, X , follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.

<h2>Input Format</h2>

The first line contains X's mean. The second line contains the value we want the probability for:

2.5<br>
5

If you do not wish to read this information from stdin, you can hard-code it into your program.

<h2>Output Format</h2>

Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e.,1.234 format).


# 2.Poisson Distribution II

<h2>Objective</h2>
In this challenge, we go further with Poisson distributions.

<h2>Task</h2>
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:
<ul>
    <li>The number of repairs, X , that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is CA=160 + 40X^2 .</li>
    <li>The number of repairs, Y , that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is CB=128 + 40Y^2.</li>
</ul>
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

<h2>Input Format</h2>

A single line comprised of 2 space-separated values denoting the respective means  for A and B:

0.88 1.55

If you do not wish to read this information from stdin, you can hard-code it into your program.

<h2>Output Format</h2>

There are two lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e.,1.234 format):
<ol>
  <li>On the first line, print the expected daily cost of machine A.</li>
  <li>On the second line, print the expected daily cost of machine B.</li>
</ol>

# 3.Normal Distribution I

<h2>Objective</h2>
In this challenge, we learn about normal distributions.

<h2>Task</h2>
In a certain plant, the time taken to assemble a car is a random variable, X , having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:
<ol>
    <li>Less than 19.5 hours?</li>
    <li>Between 20 and 22 hours?</li>
</ol>
<h2>Input Format</h2>

There are 3 lines of input (shown below):

20 2<br>
19.5<br>
20 22

The first line contains 2 space-separated values denoting the respective mean and standard deviation for X. The second line contains the number associated with question 1. The third line contains 2 space-separated values describing the respective lower and upper range boundaries for question 2.

If you do not wish to read this information from stdin, you can hard-code it into your program.

<h2>Output Format</h2>

There are two lines of output. Your answers must be rounded to a scale of 3 decimal places (i.e.,1.234 format):
<ol>
    <li>On the first line, print the answer to question 1 (i.e., the probability that a car can be assembled in less than 19.5 hours).</li>
    <li>On the second line, print the answer to question 2 (i.e., the probability that a car can be assembled in between 20 to 22 hours).</li>
</ol>

# 4.Normal Distribution II

<h2>Objective</h2>
In this challenge, we go further with normal distributions.

<h2>Task</h2>
The final grades for a Physics exam taken by a large group of students have a mean of mue=70 and a standard deviation of sigma=10. If we can approximate the distribution of these grades by a normal distribution, what percentage of the students:
<ol>
    <li>Scored higher than 80 (i.e., have a grade>80)?</li>
    <li>Passed the test (i.e., have a grade>=60 )?</li>
    <li>Failed the test (i.e., have a grade<60 )?</li>
</ol>
Find and print the answer to each question on a new line, rounded to a scale of 2  decimal places.

<h2>Input Format</h2>

There are 3 lines of input (shown below):

70 10<br>
80<br>
60

The first line contains 2 space-separated values denoting the respective mean and standard deviation for the exam. The second line contains the number associated with question 1. The third line contains the pass/fail threshold number associated with questions 2 and 3.

If you do not wish to read this information from stdin, you can hard-code it into your program.

<h2>Output Format</h2>

There are three lines of output. Your answers must be rounded to a scale of 2 decimal places (i.e.,1.23 format):
<ol>
    <li<On the first line, print the answer to question 1 (i.e., the percentage of students having grade>80).</li>
    <li<On the second line, print the answer to question 2 (i.e., the percentage of students having grade>=60).</li>
    <li<On the third line, print the answer to question 3 (i.e., the percentage of students having grade<60).</li>
</ol>
