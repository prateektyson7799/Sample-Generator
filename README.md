# Sample-Generator
function to generate simulated samples from a giving distribution
Program: dist.py
Language: Python version 3.9
Libraries: ‘Random’ only
Steps to execute the program:
1. Open the terminal and go to the path where the file is located.
2. Execute the file ‘dist.py’ through python3.
Python3 dist.py
3. The command line input should be given in a single string format with
comma “,” considering as separation of input and in the end for
parameters.
3,10,binomial,10,0.5
4. The Sample numbers are printed on terminal and a file result.txt is also
generated in the same path of the python program file which include
sample numbers, Sample mean and Sample standard deviation.
For references:
• 3,10,bernoulli,0.5 – Bernoulli distribution
• 3,10,binomial,10,0.6 – Binomial distribution
• 3,15,geometric,0.8 – Geometric distribution
• 3,20,negative binomial,3,0.6 – Negative binomial
• 3,10,poisson,4 – Poisson distribution
• 3,15,arb,0.6,0.4,0.7(so on) – Arbitrary discrete
• 3,20,uniform,1,10 - uniform distribution
• 3,10,exponential,5 – exponential distribution
• 3,15,gamma,0.75,1.5 – Gamma distribution
• 3,20,normal,3.0,5.0 – Normal distribution
