## Challenge3 - Accepting Arguments and Help Responses

Use the [Star Wars API](https://www.swapi.co)
- Arguments - Code should accept at lease 2 arguments with separate functions.
- Help Message - Code should print a helpful message if one of the arguments is `help` or incorrect.
- Error Handling - Code should be able to recognize and gracefully handle incorrect inputs.
- Standardized Output - Output should be in JSON format.

---
### Usage
- Clone this repo to your local computer using `git clone https://github.com/Code-Club-Crew/challenge3.git`.
- Create a new branch using `git checkout -b <NEW-BRANCH>`.
- Add your own subfolder to the repo.
- Add your files to the subfolder.

---

### Language
User choice

Recommend using the same language as Challenge1, Go, or Python

---
### Additional Resources
https://jsonlint.com/ - for checking the format of your output

https://swapi.co/documentation - for documentation relating to SWAPI

Check your language of choice for a supporting library.

---

### HINTS
<details>
  <summary>Argument Usage Hint 1</summary>
  - Argument 1 could be used to determine the type. IE `Starship`
</details>
<details>
  <summary>Argument Usage Hint 2</summary>
  - Argument 2 could be used to determine a string to search for in the data type. IE `Destroyer`
</details>
<details>
  <summary>Argument Help Message Hint 1</summary>
  - Check that the number of arguments is correct
</details>
<details>
  <summary>Argument Help Message Hint 2</summary>
  - Check that the arguments are valid
</details>
<details>
  <summary>Help Message Hint 1</summary>
  - Create a function that checks the arguments and have a branch if an argument == `help`
</details>
<details>
  <summary>Error Handling Hint 1</summary>
  - The `except` clause of `try` loops are great for catching errors
</details>

### Example Output
```
Coming Soon
```
