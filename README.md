# To-Do List (CLI)

A simple command-line to-do list app written in Python. Add, view and remove tasks from a menu in your terminal.

## Features

- View all tasks in a numbered list
- Add new tasks
- Remove tasks by number
- Input validation: invalid choices, non-numbers and out-of-range task numbers are handled without crashing

## How to run

Requires Python 3.

```
python3 to_do_list.py
```

## Example

```
=== To-Do List ===
1. View tasks
2. Add task
3. Remove task
4. Quit
What would you like to do? 2
What task would you like to add? Finish Python exercises
Finish Python exercises has been added to Tasks!
```

## What I learned

This was my first Python project. It helped me practice:

- `while` loops and menu-driven programs
- Functions with parameters and early `return`
- Lists, dictionaries and `enumerate()`
- Input validation with `try`/`except`

## Possible improvements

- Save tasks to a file so they persist between runs
- Mark tasks as done instead of only removing them
- Support multiple lists (e.g. work and home)