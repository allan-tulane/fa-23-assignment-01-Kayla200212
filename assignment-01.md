

# CMPS 2200 Assignment 1

**Name:**_____Kayla Willis____________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  No. They are similar exponential functions but the former is a faster growth rate (and thus worse time complexity) as it will always have a higher exponent as long as n is positive
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  Yes. Because we are checking for worst case runtime and the later function is lower than/has a lower growth rate than the former, it is within the bounds and included.
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  No, the first function has a higher growth rate and thus a worse runtime. The first has a polynomial growth time and the second is a form of logarithmic growth giving the later a better worst case runtime.
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes. Because omega is the lower bound/best case check, since the first function is greater than the second, it is included within the second function.
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No. Same logic as above, the second function is higher than the first so the first cannot be included under the second functio.
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes. Same logic as above, the second function is within the upper bound of the former.


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  
This is a recursive function that takes in an integer and first checks if it is less than or 1, meaning in the fibonacci sequence it would always equal 1. If greater than 1, it finds the previous two numbers in the sequence and adds them to find the xth element in the fibonacci sequence.  
.  
.  
.  
.  
.  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  The work is O(n) because the number of iterations depends purely on n, how many times the function has to go through the list of n items. The span is the same as the work because there is no recursive call or parallelism occurring in the iterative version of the function. Each number in the list is gone through one time in sequence and the list is not changed like in the recursive version.
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  The base case has a work of O(1) as it is a simple comparison. The recursive case using the Result function is more complex but like above, relies on n for the number of inputs. It divides each side in half and uses recursion on both sides(n/2)* 2 thus the work is still O(n) based on the n. The span is also still O(n) because the worst case will be based on n, the length of the list, having no key in it. The iterative and recursive versions have the same work and span because the function wasnt parallelized.
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  If it was parallelized, the work would stay the same because the n is still the determinant of the work. Even if we parallelized and split the list into parts, the sum of its parts would still equal the total values n. The span would change though and could reduce to O(logn) because instead of the worst case meaning that the longest chain is at the very end, we could parallelize and break up the n to analyze multiple groups of n at once. It's still not constant time though since the lists do still need to be searched.
.  
.  
.  
.  
.  
.  
.  