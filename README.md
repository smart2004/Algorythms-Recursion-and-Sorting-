# algorythms-recursion-and-sorting- by smart200481 <Mikhail Sutormin>

## broken_search.py  
### Brief Task Description

Alla made a mistake when copying from one data structure to another. She stored an array of numbers in a ring buffer. The array was sorted in ascending order, and it was possible to find an element in it in logarithmic time. Alla copied the data from the ring buffer into a regular array, but shifted the data of the original sorted sequence. Now the array is not sorted. However, it is necessary to provide the ability to find an element in it for O(logn).
It can be assumed that the array contains only unique elements.
  
The task must be submitted with the Make compiler, it is selected by default, there are no other compilers in the task. The solution is sent as a file. The required function signatures are in the code stubs on disk.

You are required to implement a function that searches the broken array. Files with code stubs containing function signatures and a basic test for supported languages can be found on Yandex.Disk at the link. Note that you do not need to read data and output a response.
  
### Input Format
  
The function takes an array of natural numbers and the desired number k. The length of the array does not exceed 10000. Array elements and number k do not outweigh 10000.
In the examples:
The first line contains a number n   -- is array length.
The second line contains a positive number k is the desired element.
Third line, separated by a space, is written n natural numbers are array elements.

### Output Format
  
The function must return the index of the element equal to k, if there is one in the array (numbering from zero). If the element is not found, the function should return −1.
The array cannot be changed.
To cut off inefficient solutions, your function will run from 100000 before 1000000 once.

  
### How to launch the project:
  
##### Clone repository:

```
git clone git@github.com:smart2004/Algorythms-Recursion-and-Sorting-.git
```

##### Switch to the folder:

```
cd algorythms-recursion_and_sorting-
```

##### Launch python task:

```
NOTE: To launch the code it's required to upload it into compilator Make
```
###### NOTE: better use IDE for looking to code
  
##### Example for input:
```
NOTE: There is no input data as per code solution implemented via compilator Make
```
  
##### Example for output:
```
NOTE: There is no output data as per code solution implemented via compilator Make
```
  

## hoare_sort.py
### Brief Task Description
  
Timo decided to organize a sports programming competition to find talented interns. Tasks are selected, participants are registered, tests are written. It remains to figure out how the winner will be determined at the end of the competition.

Each participant has a unique login. When the competition ends, two indicators will be attached to it: the number of solved problems Pi and the size of the penalty Fi. The penalty is calculated for unsuccessful attempts and time spent on the task.

Timofey decided to sort the table of results in the following way: when comparing two participants, the one with more problems solved will go higher. If the number of solved problems is equal, the participant with the lowest penalty goes first. If the penalties are the same, then the first one will be the one whose login comes earlier in alphabetical (lexicographical) order.

Tim ordered sweatshirts for the winners and went to the store to pick them up the day before. In his absence, he commissioned you to implement a quick sort algorithm for the results table. Since Timothy loves sports programming and doesn't like wasting RAM, your sorting implementation cannot consume O(n) additional memory for intermediate data (this modification of quicksort is called "in-place").
  
###### How in-place quick sort works
As in the case of normal quicksort, which uses additional memory, you need to select a pivot element (eng. pivot), and then reorder the array. Let's make it so that at first there are elements that do not exceed the pivot, and then - greater than the pivot.

The sort is then called recursively on the two resulting parts. It is at the stage of dividing elements into groups in the usual algorithm that additional memory is used. Now let's figure out how to implement this in-place step.

Suppose we have somehow chosen a reference element. Let's get two pointers left and right, which will initially point to the left and right ends of the segment, respectively. Then we will move the left pointer to the right until it points to an element smaller than the reference one. Similarly, we move the right pointer to the left while it is on the element that exceeds the reference one. As a result, it turns out that to the left of left all elements exactly belong to the first group, and to the right of right - to the second. Elements with pointers are out of order. Let's swap them (most programming languages use the swap() function) and advance pointers to the next elements. We will repeat this action until left and right collide.
  
### Input Format
The first line contains the number of participants n, 1 ≤ n ≤ 100 000.
Each of the next n lines contains information about one of the participants.
The i-th participant is described by three parameters:

- a unique login (a string of small Latin letters no longer than 20)
- the number of solved problems Pi
- Fi fine
Fi and Pi are integers ranging from 0 to 10**9

### Output Format
  
For a sorted list of participants, print their logins in order, one per line.

### How to launch the project:
  
##### Clone repository:

```
git clone git@github.com:smart2004/Algorythms-Recursion-and-Sorting-.git
```

##### Switch to the folder:

```
cd algorythms-recursion_and_sorting-
```

##### Launch python task:

```
python hoare_sort.py
```
###### NOTE: better use IDE and start task @ the place
  
##### Example for input:
```
5
allen 10 100
brandon 10 200
randy 10 200
mike 9 100
james 9 100
```
  
##### Example for output:
```
allen
brandon
randy
james
mike
```  
