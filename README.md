# SSH Log Analyzer
#### Video Demo: <https://youtu.be/MjhtESCasEg>
#### Description:

### What it does

This is a small program that reads SSH logs from a Linux server. It finds failed login attempts, counts how many times each IP address tried to log in, and shows which user accounts people were trying to break into.

### How to run it

```
python project.py auth.log
```

The program saves a file called `log_results.csv` with the IP addresses and their number of failed attempts, starting from the most active one. It also prints the attacked accounts, like this:

```
Report saved to log_results.csv
Attacked user: root, 2 times
Attacked user: admin, 1 time
```

To run the tests:

```
pytest test_project.py
```

### Files

- `project.py` – the main program
- `test_project.py` – tests for my functions
- `requirements.txt` – what you need to install to run the tests

### Functions

- `extract_ip(line)` – finds the IP address in one line of the log. If there is no IP address, it returns `None`.
- `count_attempts(lines)` – counts failed login attempts for every IP address.
- `sort_attempts(attempts)` – sorts the results from the most attempts to the least.
- `count_targeted_users(lines)` – counts which accounts were attacked and how many times. It works for normal accounts like `root` and also for accounts that don't exist, which show up in the log as `invalid user`.

### Some decisions I made

At first I passed the open file to two functions, but the second function got no data, because a file can only be read through once. So now I read the file once with `readlines()` and give the same list to both functions.

I save the results to a CSV file, so I can open them later in Excel and they don't disappear when the program ends.

I noticed that the IP addresses and the user accounts are both just names with numbers, so I used the same sorting function for both instead of writing it twice.

I added `errors="replace"` when opening the log, so strange characters in real logs won't crash the program.

I tried to keep every function small and doing one thing. Because of that, testing them was easy, since I didn't need any real files for the tests.

### Why I made it

I'm just starting to learn Linux and I set up my own Ubuntu server at home. I wanted to know who was trying to log in to it, so I decided to write a program that checks the logs for me.
