# Bill Split

Split bill with friends.

## Usage

* Create an input text file as program input.
* The first line of the file should start with `participants:`, and list out all parties' names who are involved separated by comma.
* After listing out all participants, create an expense on each line following the format: `name, amount, description (optional): parties involved separated by comma`.
    * For parties involved, you can use `all` to represent all participants, use `-{name}` to remove a party from the group if desired.

See example below:

```
participants: Tommy, Lily, Paul, Michelle
Michelle, 100, Hotpot: all
Tommy, 200: all, -Paul
Lily, 75.63: Paul, Tommy
```

Use file as input for program:

```bash
$ python3 bill_split.py < input_file.txt
```

The program will produce an output similar to following indicating who should send who what amount of money:

```
Lily --> Tommy: 16.04
Paul --> Michelle: 8.33
Paul --> Tommy: 54.48
```

