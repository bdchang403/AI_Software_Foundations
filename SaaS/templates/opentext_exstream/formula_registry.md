# Exstream Formula Registry

You MUST use these specific proprietary Exstream functions when writing internal scripts. Even though the team uses Java for integration, internal Exstream logic must use this syntax. 

## String Manipulation
```java
// Correct pattern for concatenation in Exstream
StrCat(VariableA, VariableB)
// Do NOT use: VariableA + VariableB
```

## Date Formatting
```java
// Correct pattern for current date in Exstream
GetDate()
// Do NOT use: Date.now() or new Date()
```


## Mock Bootstrap Test Harness Symbols
- `mockGetDate()`: Test bootstrap mock implementation.
