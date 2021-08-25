# Arithmetic-Exam-Application-2021
## JetBrains Academy Project | Level : Medium

### About
Many people are fond of interactive learning.  The application can generate a mathematical expression for a user to solve. It implements various levels of difficulty. In addition to that, the application can save the results and show the progress of learning.

1. With the first message, the program asks for a difficulty level:

    ```
    1 - simple operations with numbers 2-9
    2 - integral squares 11-29
    ```
    
2. The user have to enter an answer.
For the first difficulty level: the task is a simple math operation; the answer is the result of the operation.
For the second difficulty level: the task is an integer; the answer is the square of this number.
In case of another input: the program will ask user to re-enter. This will repeat until the format is correct.

3. The application gives 5 tasks to a user.
4. The user receives one task, enters the answer.
If the answer contains a typo,  `Incorrect format.` will be printed and program will ask user to re-enter the answer. It will repeat until the answer is in the correct format.
If the answer is a number,  `Right!` or `Wrong!` will be printed and program will move to the next question.

5. After five answers, the program will print `Your mark is N/5.` where N is the number of correct answers.

6. Then `Would you like to save your result to the file? Enter yes or no.` will be printed. 
In case of `yes, YES, y, Yes`: the app will ask the username and write `Name: n/5 in level X (<level description>)`. (X stands for the level number) in the `results.txt` file. For example — `Alex: 3/5 in level 1 (simple operations with numbers 2-9).`





7. In case of no or any other word: the program will stop.


### Example Outputs:
The greater-than symbol followed by a space (`>` ) represents the user input. Note that it's not part of the input.
##### Example 1: 
```
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
> 11
Incorrect format.
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
> 2
11
> 121
Right!
15
> 100
Wrong!
21
> 441'
Wrong format! Try again.
21
> 441
Right!
17
> 289
Right!
13
> 169
Right!
Your mark is 4/5. Would you like to save the result? Enter yes or no.
> yes
What is your name?
> Kate
The results are saved in "results.txt".
```


