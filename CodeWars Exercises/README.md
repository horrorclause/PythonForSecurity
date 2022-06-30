# Code Wars Exercises #

Here you will find a list of Codewars exercises and their solutions.



## Convert String to Camel Case ##

*Description*:

<li>Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).</li>

*Examples*:

<li>"the-stealth-warrior" gets converted to "theStealthWarrior"</li>
<li>"The_Stealth_Warrior" gets converted to "TheStealthWarrior"</li>



## Bit Counting ##

*Description*:

<li>Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.</li>

*Examples*:

<li>The binary representation of 1234 is 10011010010, so the function should return 5 in this case</li>



## Simple Pig Latin ##

*Description*:

<li>Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.</li>

*Examples*:

```
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
```
```
pig_it('Hello world !')     # elloHay orldway !
```



## Counting Sheeps ##

*Description*:

<lli>Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).</li>

*Examples*:

```
[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
```
The correct answer would be 17



## Pillars ##

*Description*:

<li>There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar). Your function accepts three arguments:</li>

```
    1) number of pillars (≥ 1);
    2) distance between pillars (10 - 30 meters);
    3) width of the pillar (10 - 50 centimeters).
```


## Your Order Please! ##

*Description*:

<li>Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.</li>
<li>Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).</li>

<li>If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.</li>


*Examples*:

```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```

## A Wolf in Sheep's Clothing ##

*Description*:

Wolves have been reintroduced to Great Britain.
You are a sheep farmer, and are now plagued by wolves which pretend to be sheep. Fortunately, you are good at spotting them.

Warn the sheep in front of the wolf that it is about to be eaten.
Remember that you are standing at the front of the queue which is at the end of the array:

```
[sheep, sheep, sheep, sheep, sheep, wolf, sheep, sheep]      (YOU ARE HERE AT THE FRONT OF THE QUEUE)
   7      6      5      4      3            2      1
```

If the wolf is the closest animal to you, return "Pls go away and stop eating my sheep".
Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.

Note: there will always be exactly one wolf in the array.

*Examples*:

```
Input: ["sheep", "sheep", "sheep", "wolf", "sheep"]
Output: "Oi! Sheep number 1! You are about to be eaten by a wolf!"

Input: ["sheep", "sheep", "wolf"]
Output: "Pls go away and stop eating my sheep"

Input: ["wolf"]
Output: "Pls go away and stop eating my sheep"
```