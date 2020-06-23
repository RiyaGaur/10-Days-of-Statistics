# 1.The Central Limit Theorem I


<h2>Objective</h2>
In this challenge, we practice solving problems based on the Central Limit Theorem. 

<h2>Task</h2>
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of meu=205 pounds and a standard deviation of sigma=15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

<h2>Input Format</h2>

There are 4 lines of input (shown below):

9800<br>
49<br>
205<br>
15

The first line contains the maximum weight the elevator can transport. The second line contains the number of boxes in the cargo. The third line contains the mean weight of a cargo box, and the fourth line contains its standard deviation.

If you do not wish to read this information from stdin, you can hard-code it into your program.

<h2>Output Format</h2>

Print the probability that the elevator can successfully transport all 49 boxes, rounded to a scale of 4 decimal places (i.e.,1.2345 format).

# 2.The Central Limit Theorem II

<h2>Objective</h2>
In this challenge, we practice solving problems based on the Central Limit Theorem.

<h2>Task</h2>
The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of meu=2.4 and a standard deviation of sigma=2.0.

A few hours before the game starts,100  eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

<h2>Input Format</h2>

There are 4 lines of input (shown below):

250<br>
100<br>
2.4<br>
2.0

The first line contains the number of last-minute tickets available at the box office. The second line contains the number of students waiting to buy tickets. The third line contains the mean number of purchased tickets, and the fourth line contains the standard deviation.

If you do not wish to read this information from stdin, you can hard-code it into your program.

<h2>Output Format</h2>

Print the probability that 100 students can successfully purchase the remaining 250 tickets, rounded to a scale of 4 decimal places (i.e.,1.2345 format).

# 3.The Central Limit Theorem III

<h2>Objective</h2>
In this challenge, we practice solving problems based on the Central Limit Theorem.

<h2>Task</h2>
You have a sample of 100 values from a population with mean meu=500 and with standard deviation sigma=80. Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P( A < x < B)=0.95. Use the value of z=1.96. Note that z is the z-score.

<h2>Input Format</h2>

There are five lines of input (shown below):

100<br>
500<br>
80<br>
.95<br>
1.96

The first line contains the sample size. The second and third lines contain the respective mean (meu) and standard deviation (sigma). The fourth line contains the distribution percentage we want to cover (as a decimal), and the fifth line contains the value of z.

If you do not wish to read this information from stdin, you can hard-code it into your program.

<h2>Output Format</h2>

Print the following two lines of output, rounded to a scale of 2 decimal places (i.e.,1.23 format):
<ol>
  <li>On the first line, print the value of A.</li>
  <li>On the second line, print the value of B.</li>
</ol>
