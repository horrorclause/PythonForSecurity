# Python For Security

Information that is useful for learning Python.

## :books:Resources for Learning Python ##

<ul>
  <li><a href="https://www.codecademy.com">Codecademy</a></li>
  <li><a href="https://www.amazon.com/s?k=al+sweigart&sprefix=al+swe%2Caps%2C89&ref=nb_sb_ss_ts-doa-p_1_6">Al Swiegart's Python Books</a></li>
  <li><a href="https://edube.org/">Edube, Free Learning for Python, C, C++, and JavaScript</a></li>
  <li><a href="https://stackoverflow.com/">Stack Overflow</a></li>
  <li><a href="https://www.dataquest.io/">Dataquest</a></li>
  <li><a href="https://www.programiz.com/python-programming/class">Python Objects and Classes</a></li>
  <li><a href="https://www.youtube.com/watch?v=ZDa-Z5JzLYM">Python OOP Tutorial (Video)</a></li>
  <li><a href="https://realpython.com/python-pep8/">What is PEP 8?</a></li>
  <li><a href="https://exercism.org/">Exercism - Learn Multiple Programming Languages For Free</a></li>
</ul>

<br />

## :snake:Fun Sites to Practice Python ##

<ul>
  <li><a href="https://www.codewars.com/">CodeWars</a></li>
  <li><a href="https://www.codingame.com/start">Coding Game</a></li>
  <li><a href="https://rosalind.info/problems/locations/">Rosalind</a></li>
  <li><a href="https://www.hackerrank.com/auth/signup">Hacker Rank</a></li>
</ul>

<br />

## :octocat:All About Git ##

<ul>
  <li><a href="https://www.youtube.com/watch?v=HkdAHXoRtos">Git It? How to use Git and Github</a></li>
  <li><a href="https://www.youtube.com/watch?v=RGOj5yH7evk">Git and GitHub for Beginners - Crash Course</a></li>
  <li><a href="https://www.youtube.com/watch?v=a8MckiothGc">How to use GitHub with Pycharm in less than 7 minutes</a></li>
  <li><a href="https://git-scm.com/book/en/v2">Download the Pro Git Book</a></li>
</ul>

### Don't Forget to Set Your Global Git Username and Email ###
The first time you connect your GitHub to your IDE you will need to set your global username and email
before you can push out any commits:
```
git config --global user.name "Enter Your Name Here"
git config --global user.email "Enter youremail@yourdomain.com Here"
```

<br />

## :computer:Regular Expressions (RegEx), What is it? ##

<ul>
  <li><a href="https://towardsdatascience.com/a-very-easy-tutorial-to-learn-python-regular-expression-re-c42fbbc01ef2">Python RegEx Tutorial</a></li>
  <li><a href="https://www.w3schools.com/python/python_regex.asp">W3Schools Python RegEx</a></li>
  <li><a href="https://realpython.com/regex-python/">Real Python - RegEx</a></li>
  <li><a href="https://www.youtube.com/watch?v=AEE9ecgLgdQ">Regular Expressions in Python (Video)</a></li>
  <li><a href="https://regex101.com/">Regex 101 - Write and Test Your RegEx</a></li>
</ul>

<br />

## :pushpin:Helpful Hints ##

### Installing VirtualBox Guest Additions in Kali ###

From a terminal window, copy the VboxLinuxAdditions.run file from the Guest Additions CD-ROM to a path on your local system.
Ensure it is executable and run the file to begin the installation.

```
kali@kali:~$ cp /media/cdrom/VBoxLinuxAdditions.run ~/Downloads/
kali@kali:~$ chmod 0755 ~/Downloads/VBoxLinuxAdditions.run
kali@kali:~$ cd ~/Downloads/
kali@kali:~/Downloads$ ./VBoxLinuxAdditions.run
```

Reboot the Kali Linux VM to complete the Guest Additions installation.
You should now have full mouse and screen integration as well as the ability to share folders with the host system.
Make sure to remove the disk from the virtual drive once logged back into the system.

<br />

### Installing VSCode on Kali ###

The first step is to download the ".deb" package from:

<ul>
  <li><a href="https://code.visualstudio.com/download">VSCode Downloads</a></li>
</ul>

![image](https://user-images.githubusercontent.com/10188810/178114902-37117e8f-5221-453b-9afc-9605bdecfb69.png)

This file will now be located in your Downloads folder. Verify this and install the file (Note that your installer may be a different version than this):

![image](https://user-images.githubusercontent.com/10188810/178114927-e76290c2-1e98-48d0-9d69-d3dd98d995fe.png)

```
cd Downloads  # navigate to your Downloads folder
ls  # List out all the items in the folder
sudo apt install ./code_1.69.0-1657183742_amd64.deb  # install the package

```

That's it! VSCode is now installed on your machine, feel free to delete the installer package in your "Downloads" folder. You will now be able to find VSCode in your "Applications" by searching in the top left corner.

![image](https://user-images.githubusercontent.com/10188810/178114958-a6a02555-6de9-48f3-bc54-4657807dea5f.png)


