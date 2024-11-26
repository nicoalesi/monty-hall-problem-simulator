# Monty Hall Problem Simulator

Monty Hall Problem Simulator is a simulator that calculates the two possible
decisions' win rates in Monty Hall famous problem.

It is designed to make you understand the reason why you should always change door
after the host reveals one of the goats.

## Index
- [Usage](#usage)
- [Monty Hall Problem](#monty-hall-problem)
- [My Explanation](#my-explanation)

----

## Usage

To use this program follow these steps:

1. Download all the files from GitHub.
2. Open the terminal.
3. Move to the directory where the project is located.
4. Make sure to have python installed on your computer.
5. Run the main file ***simulator.py*** using the following command:

   `python simulator.py`

&nbsp;
##### *The program takes the number of simulations you want to try as input.*

## Monty Hall Problem

The Monty Hall problem is a probability puzzle with a counter intuitive solution.

What is it about? Suppose you are taking part to a show and you have three doors in front of you:
behind two of them there are goats, behind the remaining one there is a car. You get to take whatever
is behind the door you choose. Unexpectedly after you make your choice, the host of the show reveals
what is behind one of the other two doors; he knows where the car is and makes sure to reveal only
the goat's door every time. At this point he asks you whether you want to change door or keep the one
you chose earlier.

## My Explanation

Even though you might think that the change is useless and irrelevant it is not. You might
think that now the probability of winning is 50% because of the two remaining choices, but
it is not. 

Indeed, if you decide to change your choice, the probability of winning will be **66%**.

My approach to this is really simple and it is what can be deduced from my code. To calculate
the probability of winning changing the door we can calculate the complementary of the 
probability of winning keeping our first door. When you choose your door you have 3 possibilities,
hence 33% chance of getting the winning one. If you don't do anything at all after your decision
it doesn't matter what the host shows, you still have your 1/3 probability of winning. This means
that if we don't change and lose, we would have won changing door: This is because you can either win
or lose, and if you don't win keeping your door, you lose keeping it. We can say that if you had a
33% chance of winning before, changing the door you will have a 66% chance, just because if you do
one you're not doing the other.
