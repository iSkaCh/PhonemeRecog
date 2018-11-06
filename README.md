# PhonemeRecog
School project. This work is a proof of concept for end to end phoneme recognition using Reccurent Neural Networks ( without MFCC ). So far only the bi-directional Gated Reccurent unit (BGRU) model was tested, we achieve a 57% on 10k batchs accuracy on the whole TIMIT Test set after roughly 16hours of training on a GTX 950M GPU. A paper already studied the use of Convolutional Neural Networks ( https://arxiv.org/pdf/1312.2137.pdf ) achieving up to 70% accuracy.





For TIMIT nist to riff conversion ( windows ) : 
 
1- install sox.

2- add sox to path. Temporary solution : 
```bash
SET PATH=%PATH%;"C:\path to sox folder"
```
3- go to directory containing TIMIT data.

4- run this command. ( not the fastest but does the trick ) 
```bash
forfiles /s /m *.wav /c "cmd /c sox  @file @fnameRIFF.wav"
```
#Mirror
This code tries to solve the Mirror problem. Also known as "a safe bet" problem (I looked after finishing my work and not before ! ).
I implement an intuitive solutions and not a mathematical one, so scalability to other problems may be limited. 
Though, this solution is inspired by graph search algorithms that start from the source and the destination.

This solution is not optimal for both memory and speed (for example i use cout which is slowed than printf).

To run the code you can try to use the provided executable. Or you can compile it yourself:

##The main ideas
###Finding a solution
To find a solution the idea that i came up with is simple: a solution exist where 2 rays, one from the source and a second from the destination, meet. 
This idea works even when we have multiple solutions.
suppose we have the following mirror :

 --- --- --- --- --- ---
| . | \ |   |   |   |   |
 --- --- --- --- --- ---
|   | . | / | * | \ |   |
 --- --- --- --- --- ---
|   | . | * |   | * |   |
 --- --- --- --- --- ---
|   | \ | X | \ | * |   |
 --- --- --- --- --- ---
|   |   | \ | X | \ | * |
 --- --- --- --- --- ---
where "." is a direct ray.
	  "*" is a reverse ray.
	  "X" a solution.
We can see that the rays from both side bounce until they reach the mirror.

### Propagation of rays
	The idea of the propagation is simple, we go in one direction and if we meet a mirror we change the direction.
	The trick here is that the manner with which the mirrors change the direction of the rays depends on the nature of the mirror in a really practical way:
		for \ mirrors : if the ray come from a + direction the direction stays  + and if from - direction it give - direction. We multiply the direction by 1
		as for / mirrors : if the ray come from a + direction the direction becomes - and if from - direction it give + direction. We multiply the direction by -1
		
## Implementation		
### The main class
	The main class is a safe containing elements matrix, the number of rows and columns and its id. (well a UML diagram may have been better, but we only have one class)
	The elements matrix, which is actually a vector of vectors, contain mirrors, and can contain information about the ray and solutions. From what we said earlier :
		-1 means the element is a / mirror.
		1 means the element is a \ mirror.
		2 means we have a horizontal ray
		-2 means vertical ray
		4 a solution

###Printing
	Other than giving the solutions. I added some printing and visualisation. First, some text to guide the user. Second, a method to print the safe.


	
##Conclusion
	This work was really fun, I never thought that i had missed coding in c++ this much. I tried to play a little trying multiple stl structure and so on. 
	I know that there are more scalable solutions that would use fenwick tree search, but i thought that implementing my intuitive solution would better present me.
	Hope you like my humble work! (Also i (s)pray for no bugs x) )
	
