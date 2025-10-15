> Book with same title by cpp creator

---

# Preface

- Often, a Problem is only fully understood after programming a solution for it first.

# 0 Notes to the Reader

---

- Programming is a craft, and craftsmen _need_ to understand their tools.

- Humans learn form the concrete faster than they learn from the abstract.

- You will run before you walk, see how babies learn to walk, they dash before they learn how to refine their walking technique.

- If you aim to write code at the highest level of abstraction possible you need a real good understanding of the low-level facilities and techniques.

- Learning any Major and valuable skill takes time.

- Programming is part of the effort to understand a problem.

---

# Part I: the Basics

## Chapter 1: Hello World!

- Programming is learned by writing programs - Brian Kernighan.

> it seems like the used compilation method does not work on my ubuntu machine, lemme check for it on the OM one, does not work there either... lol.

- Strings are set by "...".

- `cout` === character output stream.

- `<<` output operator.

- `//` are comments.

- code is for reading, do all you can to make it readable.

- write a comment with the outline of what is being done in this file.

- a function is a sequence of instructions, and it has:

    - a return type.

    -  a name.

    - a parameter list.

    - a function body.

- a return value of zero informs the system that the program terminated successfully.

- the compiler is your best friend.

- sourcefile1 & sourcefile2 -> compiler -> objectcode1 objectcode2 -> linker -> execfile

- compiler errors are called compile-time errors, while linkers' are link-time errors and the errors which are found on run are called run-time errors.

### Review answers

1. outputting 'Hello, World!' onto the monitor.
2. return type, name, parameter list, instructions.
3. main.
4. declaring success.
5. make object code.
6. giving access to the stdlib.
7. a backwards compatible version of `import`.
8. a source code file.
9. links the object files into executable program.
10. source file is a .cpp file and is readable if you know cpp, while object files are not humanely readable.
11. a source code file compiled and linked.
12. integrated dev env, makes everything in a one place.
13. executing it (from the terminal or gui).
14. a line of code which the compiler will ignore.
15. to make you more accustomed with the language and the tooling.
16. programmin is a craft, duh!

### Exercises

1. first-program-edit.cpp
2. go-to-bathroom.cpp
3. go-to-uni.cpp
4. bake-cookies.cpp
5. terms-definition.md

## Chapter 2: Objects, Types, and Values

- an object is a region of the memory with a type that specifies its kind.

- a variable is a named object.

- a type defines the scope of the object.

> read-write-first-name.cpp

- a prompt is a messages that makes the user do something.

- a definition is a statement that makes a new variable.

- `cin` is standard charachter input.

- `>>` is the 'get-from' operator.

- a value is what is stored in a variable.

- a definition should usually provide initial value.

- the simplest five types in cpp are:

    - int - series of numbers

    - double - floating point number

    - char - a single char in single quotes `'x'`

    - string - seq of char in double quotes `"x"`

    - bool - `true` or `false`

> read-name-age.cpp

- in line 9, the name and age can be read in one actual line, because a string is ended with a whitespace... so inputting "john doe 33" would result in a 'hello, john (age: 0)!'.

- a string read by `>>` will end with the first whitespace it sees.

- a string is init'd by default to `""`.

- the type dictates the operations we are allowed to use on a specific variable.

- in strings a `+` means concat.

> repeated-words-checker.cpp

- when solving a problem, try to not start from scratch, look for a similar problem and adapt its solution accordingly.

- a variable name must start with a letter and can only contain letters, digits, and underscores.

- our types are usually `Name` to seperate them from the stdlib implementation.

- avoid: 0 o O I 1 l since they might cause confusion (depends on the font yk).

> widen-narrow.cpp

- if the type is obvious, use `auto`.

### Drill

- message-template

### Review

1. something which makes the user take action.
2. `=`.
3. `=`.
4. :
```cpp
int number;
cout << "enter the number";
```
5. newline.
6. a whitespace
7. a whitespace or a comma.
8. `cout << "Hello, " << name << "!\n";`.
9. a space of memory with a type.
10. 'strings and chars'
11. 'strings and chars'
12. obj with a name.
13. byte, 4 bytes, 8 bytes (8 bit, 32 bit, and 64 bits)
14. we widen them when we want to store info which is bigger that what they can handle.
15. assignment and comparing.
16. a statement which has a typename and a name
17. init is done with the def, assignment is done after def.
18. it is making two strings or more into one string, done with `+`.
19. \+ \- \* / % == <= >=.
20. Legal names:
    1. This_little_pig
    2. This_1_is_fine
    3. MineMineMine
    4. number
20.1:
    - coz `@`
    - coz `?`
    - coz starts with `_`
    - coz `.`
    - coz starts with `2`
    - coz `$`
    - coz has space
21. legal but we don't use:
    1. foo
    2. f00
    3. fOO
    4. Ill
    5. 1ll
22. short and cuts to the chase.
23. making sure that the value of the variable is in cohesion with its type.
24. because we go from 64 bits to half of that, so we lose information.
25. if the type is bigger in size then yes, else no.
26. taking note of every defined var, or defining on the largest scope.
27. when the type is obvious.

### Exercises

1. try-this.
2. mile-to-km.cpp
3. no-legal-names.cpp
4. operations-on-ints.cpp
5. operations-on-doubles.cpp
6. sort-three-ints.cpp
7. sort-three-strings.cpp
8. even-odd.cpp
9. speech-to-ints.cpp
10. post-fix-calc.cpp
11. money-calc.cpp

## Chapter 3: Computation

- we are here interested in the `input -> Program [ code -> code -> code ] -> output`.
- inputs into a part of a program are called arguments, and outputs are called results.
- computation is the act -art- of producing results based on some inputs.
- a programmer's job is to express computations:
    1. correctly.
    2. simply.
    3. efficiently.
- a program needs to be in its simplest form, since it will be transmuted with time.
- the job becomes a responsibility when we decide to go pro with our coding.
- concerns of structure and code quality will likely make debugging easier and less frustrating.
- the main tool for organizing a program is to break a huge computation into many little one, and we have two techniques for that:
    1. abstraction: the act of hiding details which we will not use behind a convenient general interface.
    2. divide and conquer: splitting the program into manageable sizes.
- we split the huge problems because we can forget where we were or how we came here if we work on the huge problem in one go.
- concerns about structure lie at the heart of good software and ignoring it can get real expensive real quick.
- building with no structure is like building with mud bricks, you will not get to the tenth floor, ever.
- an expression computes a value from a number of operands.
- if the result of an expression is nonsense but the expression itself is syntactically correct you will have nonsense which the compiler will not care about, since it does not know what you are trying to compute.
- ugly code slows down reading and comprehension and often hides logical errors.
- you can define constants using `constexpr <type> <var-name> = <value>;`.
- avoid magical constants, neither you nor others will remember its meaning after three hours.
- a `constexpr` must have a value at compile time, but if you want another way to define constants then use `const <type> <var-name> = <value>;`.
> `f<T>(a)` is a function template call, which passes `a` to `f<T>` as an arg.
> `[](a){S}` is a lambda expression, which creates a function object with `a` as an argument.
> `T{a}` where `T` is a type widens `a`.
> `a<b<c` means `(a<b)<c`, which means `(true | false)<c` which makes no sense, do not use that.
- 'watch out for the error and hope your compiler warns' lol.
- we can select with either `if` or `switch` statements.
- the simplest form of selection is an if-statement, consider the following code:
```cpp
int a = 0;
int b = 0;
cout << "Please enter two ints";
cin >> a >> b;
if ( a < b )
    cout << a << " is smaller than " << b << '\n';
else
    cout << a << " is larger than " << b << '\n';
```
- you can also do an else-if like this:
```cpp
if (cond)
    code;
else if (cond2)
        code2;
else
    code3;
```
- you demonstrate your competence by writing the simplest correct program there is.
- we can rewrite our three-way-if'ing into an elegant `switch` statement.
- we can only switch on ints, chars, and enums.
- the values in the case labels must be constant expressions.
- you can not use the same value for two case labels.
- you can use multi-case-labels for a single case.
- never forget to end each case with a `break`.
- iteration is the act of doing something more than one time.
```cpp
int main()
{
    int i = 0;
    while ( i < 100 ){
        cout << i << '\t' << square(i) << '\n';
        ++i;
    }
}
```
- the while loop has a condition and a body.
> char-iteration.cpp
- we could have written the example like this:
```cpp
int main () 
{
    for ( int i = 0; i < 100; ++i){
        cout << i << '\t' << square(i) << '\n';
    }
}
```
- a function is a named squence of statements and can return a value.
- for the used `square` funciton above we can define:
```cpp
int square( int x ){
    return x * x;
}
```
- the compiler is designed such that the code once compiled will always give the same result, it is determenistic by design.
- the parameter list can be empty, and we use `void` for functions that return nothing:
```cpp
void wirte_sorry(){
    cout << "Sorry!\n";
}
```
> sq-add.cpp
- we can define a function:
```cpp
int square(int);
double sqrt(double);
```
- as such, we can store our functions elsewhere and only focus on what we need to do.
- a vector is cpp's version of a list, and we define it like this:
```cpp
vector <int> v = {5, 7, 4, 6, 8};
```
- we can only store one type of data in a vector with a specified type.
- we can init a vector without data, so we have its size ready to be used.
- a vector knows its size, so we can use:
```cpp
vector <int> v = {5, 7, 4, 6, 8};
for ( int i = 0; i < v.size() ; ++i )
    cout << v[i] << '\n';
// OR
for ( int x : v)
    cout << x << '\n';
```
- the last example is called a range-for-loop.
- we can add elements to a vector by using the `push_back()` function, i.e.:
```cpp
vector <double> v;
v.push_back(6.5);
v.push_back(2.7);
```
- we can make a vector which we do not know its size and would like to enter the data into it like this:
```cpp
vector <double> temps;
for ( double temp; cin >> temp )
     temps.push_back(temp);
    // do something
```
> see vector-calcs.cpp
- when iterating always remember the case of no elements.
> simple-dict.cpp

> DRILL

- [ ] make a bleeping prog, which reads words and prints them out untill it sees a bad one which will be replaced.
- [ ] add chf conversion to money-conversion-switch.cpp

## Chapter 4



## Chapter 5



## Chapter 6



## Chapter 7



## Chapter 8



---

# Part II



---

# Part III
