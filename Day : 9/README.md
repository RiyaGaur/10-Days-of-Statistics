# Multiple Linear Regression

<h2>Objective</h2>
In this challenge, we practice using multiple linear regression. Check out the Tutorial tab for learning materials!

<h2>Task</h2>
Andrea has a simple equation:<br>
            <strong>Y= a + b1 . f1 +b1 . f2 + ... +bm . fm</strong><br>
for (m + 1)  real constants (a ,f1 ,f2 ,... ,fm ). We can say that the value of Y depends on m features. Andrea studies this equation for n different feature sets (f1 ,f2 ,... ,fm ) and records each respective value of Y. If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?
Note: You are not expected to account for bias and variance trade-offs.

<h2>Input Format</h2>

The first line contains 2 space-separated integers, m(the number of observed features) and  n(the number of feature sets Andrea studied), respectively.
Each of the n subsequent lines contain m+1 space-separated decimals; the first m elements are features (f1 ,f2 ,... ,fm ), and the last element is the value of Y for the line's feature set.
The next line contains a single integer, q , denoting the number of feature sets Andrea wants to query for.
Each of the q subsequent lines contains m space-separated decimals describing the feature sets.

<h2>Constraints</h2>
<ul>
            <li>1<=m<=10</li>
            <li>5<=n<=100</li>
            <li>0<=xi<=1</li>
            <li>0<=Y<=10^6</li>
            <li>1<=q<=100</li>
 </ul>

<h2>Scoring</h2>
For each feature set in one test case, we will compute the following:
<ul>
            <li>di^'=|computed value of Y - expected value of Y|/expected value of Y</li>
            <li>di=max(di^' - 0.1, 0).We will permit up to a +-10% margin of error.</li>
            <li>si=max(1.0 - di, 0)</li>
                        
</ul>           
          
The normalized score for each test case will be:S=(summation i=1 to q si)/q . If the C challenge is worth  points, then your score will be SXC .

<h2>Output Format</h2>

For each of the q feature sets, print the value of Y on a new line (i.e., you must print a total of q lines).
