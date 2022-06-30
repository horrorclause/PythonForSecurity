# Code Wars Exercises #

Here you will find a list of Codewars exercises and their solutions.



### Convert String to Camel Case ###

*Description*:

<li>Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).</li>

*Examples*:

<li>"the-stealth-warrior" gets converted to "theStealthWarrior"</li>
<li>"The_Stealth_Warrior" gets converted to "TheStealthWarrior"</li>



### Bit Counting ###

*Description*:

<li>Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.</li>

*Examples*:

<li>The binary representation of 1234 is 10011010010, so the function should return 5 in this case</li>



### Simple Pig Latin ###

*Description*:

<li>Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.</li>

*Examples*:

```
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
```
```
pig_it('Hello world !')     # elloHay orldway !
```



### Counting Sheeps ###

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