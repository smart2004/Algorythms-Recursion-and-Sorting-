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
git clone git@github.com:smart2004/Algorythms-Recursion_and_Sorting-.git
```

##### Switch to the folder:

```
cd algorythms-recursion_and_sorting-
```

##### Launch python task:

```
python broken_search.py
```
###### NOTE: better use IDE and start task @ the place
  
##### Example for input:
```
6
0 4 1 10 0 8
```
  
##### Example for output:
```
0 1 2 1 0 1
```
  

## hoare_sort.py
### Brief Task Description

The "Speed Typing Trainer" is a sixteen-key 4x4 square keyboard. Each key can display either a dot or a number from 1 to 9.
The exercise on the simulator is divided into rounds:
- each round consists of several games;
- in different rounds, the number of games may be different;
- the number of each game in the round is indicated by the counter t.
  
For each round, certain values are set on the keys, which remain unchanged during all the games of the round.
The value of the game counter t cannot exceed the value of the largest number displayed on the keyboard in the current round.
Two players take part in the exercise on the simulator, they play together on the same keyboard. For each round, the maximum number of keys that one player can press is set (it is denoted by the variable k and does not change during the round).
In each individual game, the participants must press the keys together, on which the number corresponding to the number of the game t is displayed. For example, in the second game of a round, players must press all those keys that show a deuce.
There may be games in the round where you do not need to press buttons: for example, in the above version of the round in games from t = 4 to t = 8, you do not need to press buttons: there are no numbers from 4 to 8 on the keyboard.
If in the next game the participants have the opportunity to press all the necessary keys, they press them and get 1 point.
Let's assume that for the round a set of buttons is given, as in the picture, and k = 3 (each of the participants can press no more than three buttons). Then in the second game (t = 2), where twos must be pressed, two players can only press 6 keys together (k * 2 = 6). But there are seven twos on the keyboard; participants will not be able to click all of them and will not receive a point.
  
Write a program that will receive data for a specific round:
- k value,
- values for buttons,
and calculate the number of points that will be earned in this round.
  
### Input Format
  
The first line contains an integer k (1 ≤ k ≤ 5).

The next four lines set the values for the buttons—4 characters per line. Each character is either a dot or a number from 1 to 9. The characters on the same line are consecutive and are not separated by spaces.

### Output Format
  
Print a single integer, the number of points the players will score in the round.

### How to launch the project:
  
##### Clone repository:

```
git clone git@github.com:smart2004/Algorythms-Basics-.git
```

##### Switch to the folder:

```
cd algorythms-basics-
```

##### Launch python task:

```
python hoare_sort.py
```
###### NOTE: better use IDE and start task @ the place
  
##### Example for input:
```
3
1231
2..2
2..2
2..2
```
  
##### Example for output:
```
2
```  
