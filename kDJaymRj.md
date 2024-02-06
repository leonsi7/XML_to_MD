## Constants

### Dormandprince54

**Category**: Math Constants

**Result**: DormandPrince54 solver

**Returns**: None

---
### Threeeighthes

**Category**: Math Constants

**Result**: ThreeEighthes solver

**Returns**: None

---
### Luther

**Category**: Math Constants

**Result**: Luther solver

**Returns**: None

---
### Adamsbashforth

**Category**: Math Constants

**Result**: AdamsBashforth solver

**Returns**: None

---
### Euler

**Category**: Math Constants

**Result**: Euler solver

**Returns**: None

---
### Adamsmoulton

**Category**: Math Constants

**Result**: AdamsMoulton solver

**Returns**: None

---
### Graggbulirschstoer

**Category**: Math Constants

**Result**: GraggBulirschStoer solver

**Returns**: None

---
### Rk4

**Category**: Math Constants

**Result**: rk4 solver

**Returns**: None

---
### Dp853

**Category**: Math Constants

**Result**: dp853 solver

**Returns**: None

---
### Gill

**Category**: Math Constants

**Result**: Gill solver

**Returns**: None

---
### Midpoint

**Category**: Math Constants

**Result**: Midpoint solver

**Returns**: None

---
### Highamhall54

**Category**: Math Constants

**Result**: HighamHall54 solver

**Returns**: None

---
## Operators

### Iterator Operators

### Random Operators

#### gamma_density

**Concept**: Random

**Arguments**:
- *x* (-13)

**Result**: gamma_density(x,shape,scale) returns the probability density function (PDF) at the specified point x of the Gamma distribution with the given shape and scale.

**Returns**: None

**Usage Examples**:

 - Code: ```
gamma_density(1,9,0.5) ```
 
 - Returns:  ```
0.731 ```


---
#### gamma_rnd

**Concept**: Random

**Arguments**:
- *shape* (-13)

**Result**: returns a random value from a gamma distribution with specified values of the shape and scale parameters

**Returns**: None

**Usage Examples**:

 - Code: ```
gamma_rnd(9,0.5) ```
 
 - Returns:  ```
0.731 ```


---
#### weibull_rnd

**Concept**: Random

**Arguments**:
- *shape* (-13)

**Result**: returns a random value from a Weibull distribution with specified values of the shape (alpha) and scale (beta) parameters. See https://mathworld.wolfram.com/WeibullDistribution.html for more details (equations 1 and 2). 

**Returns**: None

**Usage Examples**:

 - Code: ```
weibull_rnd(2,3)  ```
 
 - Returns:  ```
0.731 ```


---
#### exp_density

**Concept**: Random

**Arguments**:
- *x* (-13)

**Result**: returns the probability density function (PDF) at the specified point x of the exponential distribution with the given rate.

**Returns**: None

**Usage Examples**:

 - Code: ```
exp_density(5,3)  ```
 
 - Returns:  ```
0.731 ```


---
#### lognormal_rnd

**Concept**: Random

**Arguments**:
- *shape* (-13)

**Result**: returns a random value from a Log-Normal distribution with specified values of the shape (alpha) and scale (beta) parameters. See https://en.wikipedia.org/wiki/Log-normal_distribution for more details. 

**Returns**: None

**Usage Examples**:

 - Code: ```
lognormal_rnd(2,3) ```
 
 - Returns:  ```
0.731 ```


---
#### weibull_trunc_rnd

**Concept**: Random

**Arguments**:
- *shape* (-13)
- *shape* (-13)

**Result**: 
returns a random value from a truncated Weibull distribution (in a range or given only one boundary) with specified values of the shape (alpha) and scale (beta) parameters. See https://mathworld.wolfram.com/WeibullDistribution.html for more details (equations 1 and 2). 

**Returns**: 


---
#### lognormal_density

**Concept**: Random

**Arguments**:
- *x* (-13)

**Result**: lognormal_density(x,shape,scale) returns the probability density function (PDF) at the specified point x of the logNormal distribution with the given shape and scale.

**Returns**: None

**Usage Examples**:

 - Code: ```
lognormal_density(1,2,3)  ```
 
 - Returns:  ```
0.731 ```


---
#### weibull_density

**Concept**: Random

**Arguments**:
- *x* (-13)

**Result**: weibull_density(x,shape,scale) returns the probability density function (PDF) at the specified point x of the Weibull distribution with the given shape and scale.

**Returns**: None

**Usage Examples**:

 - Code: ```
weibull_rnd(1,2,3)  ```
 
 - Returns:  ```
0.731 ```


---
#### exp_rnd

**Concept**: Random

**Arguments**:
- *rate* (-13)

**Result**: returns a random value from a exponential distribution with specified values of the rate (lambda) parameters. See https://mathworld.wolfram.com/ExponentialDistribution.html for more details ). 

**Returns**: None

**Usage Examples**:

 - Code: ```
exp_rnd(5)  ```
 
 - Returns:  ```
0.731 ```


---
#### gamma_trunc_rnd

**Concept**: Random

**Arguments**:
- *shape* (-13)
- *shape* (-13)

**Result**: returns a random value from a truncated gamma distribution (in a range or given only one boundary) with specified values of the shape and scale parameters.


**Returns**: 


---
#### lognormal_trunc_rnd

**Concept**: Random

**Arguments**:
- *shape* (-13)
- *shape* (-13)

**Result**: 
returns a random value from a truncated Log-Normal distribution (in a range or given only one boundary) with specified values of the shape (alpha) and scale (beta) parameters. See https://en.wikipedia.org/wiki/Log-normal_distribution for more details. 

**Returns**: 


---
### Edp-Related Operators

#### diff2

**Concept**: Equation
**Concept**: Math

**Arguments**:
- *var* (-13)

**Result**: A placeholder function for expressing equations

**Returns**: None

---
#### diff

**Concept**: Equation
**Concept**: Math

**Arguments**:
- *var* (-13)

**Result**: A placeholder function for expressing equations

**Returns**: None

---
### Matrix-Related Operators

#### .

**Concept**: Matrix

**Arguments**:
- *a* (-13)

**Result**: None

**Returns**: None

---
#### eigenvalues

**Concept**: Matrix

**Arguments**:
- *m* (-13)

**Result**: The list of the eigen values of the given matrix

**Returns**: None

**Usage Examples**:

 - Code: ```
eigenvalues(matrix([[5,-3],[6,-4]])) ```
 
 - Returns:  ```
[2.0000000000000004,-0.9999999999999998] ```


---
#### determinant

**Concept**: Matrix

**Arguments**:
- *m* (-13)

**Result**: The determinant of the given matrix

**Returns**: None

**Usage Examples**:

 - Code: ```
determinant(matrix([[1,2],[3,4]])) ```
 
 - Returns:  ```
-2 ```


---
#### inverse

**Concept**: Matrix

**Arguments**:
- *m* (-13)

**Result**: The inverse matrix of the given matrix. If no inverse exists, returns a matrix that has properties that resemble that of an inverse.

**Returns**: None

**Usage Examples**:

 - Code: ```
inverse(matrix([[4,3],[3,2]])) ```
 
 - Returns:  ```
matrix([[-2.0,3.0],[3.0,-4.0]]) ```


---
#### append_vertically

**Concept**: Matrix

**Arguments**:
- *a* (-13)

**Result**: A matrix resulting from the concatenation of the columns  of the two given matrices. 

**Returns**: None

**Usage Examples**:

 - Code: ```
matrix([[1,2],[3,4]]) append_vertically matrix([[1,2],[3,4]]) ```
 
 - Returns:  ```
matrix([[1,2,1,2],[3,4,3,4]]) ```


---
#### trace

**Concept**: Matrix

**Arguments**:
- *m* (-13)

**Result**: The trace of the given matrix (the sum of the elements on the main diagonal).

**Returns**: None

**Usage Examples**:

 - Code: ```
trace(matrix([[1,2],[3,4]])) ```
 
 - Returns:  ```
5 ```


---
#### transpose

**Concept**: Matrix

**Arguments**:
- *m* (-13)

**Result**: The transposition of the given matrix

**Returns**: None

**Usage Examples**:

 - Code: ```
transpose(matrix([[5,-3],[6,-4]])) ```
 
 - Returns:  ```
matrix([[5,6],[-3,-4]]) ```


---
#### append_horizontally

**Concept**: Matrix

**Arguments**:
- *a* (-13)

**Result**: A matrix resulting from the concatenation of the rows of the two given matrices.

**Returns**: None

---
### Containers-Related Operators

#### internal_integrated_value

**Concept**: Equation

**Arguments**:
- *agent* (-13)

**Result**: For internal use only. Corresponds to the implementation, for agents, of the access to containers with [index]

**Returns**: None

---
