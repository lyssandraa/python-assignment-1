Develop and implement a Python program to handle input/process/output to calculate the draft of a barge.  

Given an iron barge defined in terms of inputs in metres for: length (L), breadth (B) and height (H), calculate and output the draft. (The draft is the depth by which the barge sinks into the water – see diagram below). 

The barge is basically an ‘empty box’ with no lid. It has four walls and one floor.  

External factors such as the superstructure, the density of the water, combined weight of personnel, cargo etc do not need to be factored in.

(See image in folder)

Input: 
Three inputs via the keyboard using suitable prompts to the user. No validation is required - assume input of valid numeric values. It is okay if the program ’crashes’ on invalid data. 

 

Process (Calculations): 
a. iron weighs 1.06kg per metre squared 
b. draft is the mass of barge divided by: the length multiplied by the breadth 
c. mass is the surface area of barge multiplied by the weight of iron 
d. surface area is the total of area of each wall plus the area of the floor 

 

Output: 
There should be four outputs – in this order: 
The values that were input (this is called ‘echoing back’) 
The surface area calculated 
The mass calculated 
The draft calculated 
 

Output design should be clear, and user focussed. 

The assessment looks for:
Ability to program a sequence construct (do not employ validation,
selection or iteration constructs)
Efficient use of variables to handle the input data and the use of these
variables to make the code clear and readable, thus aiding maintenance
and debugging
Appropriate input/processing in the use of cascading calculations to give
a correct (and accurate) solution.
A cascading calculation takes the first input to produce an answer and this
answer is used by the second input to produce the next answer. This next
answer is used by the calculation that follows it etc.
Appropriate output that benefits user understanding
In-line comments, used sparingly, but effectively:
i.e. do not comment every single line and don’t comment lines where it is
‘obvious’ what the code is doing. Explain any ‘tricky bits’ that another
programmer may find confusing.
Clear and simple coding often means no major commentary is needed.
Appropriate testing to determine accuracy and/or problems.