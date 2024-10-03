# Exploit 4: A... SECRET PHASE?

While reviewing the source code of the **bomb** binary as the *laurie* user, we notice a function named `secret_phase`, so let's investigate further!

## Hacking the *bomb*

Upon closer inspection, we notice that within the function *phase_defused()*, there's a condition that scans a string named "s" and checks if its second argument matches the string "austinpowers". It’s clear that "s" is a global variable since it's not declared locally in the function. Additionally, this variable is only used during *phase4()* of the bomb. Therefore, to bypass this condition, we simply need to provide the string "austinpowers" after correctly solving this phase.

Answer: `9 austinpowers`

After completing all 6 phases of the bomb, the program prompts us with the secret phase.\
Let’s examine the source code for the *secret_phase()*! Initially, the input string is converted into a long integer. This integer, minus one, must be greater than 1000. Then, the input number is compared with the values of all nodes in a binary tree, which is stored as a global variable. After some testing, we find the value to solve this phase.

Answer: `1001`

Finally, continue from where we discovered the password for **thor** in [writeup1](../writeup1.md).