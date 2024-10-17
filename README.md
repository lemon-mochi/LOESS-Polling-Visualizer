To run
```
python3 plotter.py <csv file with polling data> <OPTIONAL: Colour for candidate/party 1> <OPTIONAL: Colour for candidate/party 2> <OPTIONAL: Colour for candidate/party 3> ...
```

## Libraries needed
Pandas, statsmodel, matplotlib, colour

## Other
Data containing the polls does not need to be sroted. The program will randomly generate a colour if the user does not specify a colour in the command line or if python cannot understand the colour that was given. For example, if the user types `adlfkjdkflj` as a colour, the program ignores it and generates a random colour. The input csv file must not have any empty columns and must only contain numbers in the data. For instance, `54` is allowed in the input csv file but not `54%`. I might do something to fix the problems with empty columns and percent signs later.

## Example
```
python3 plotter.py input/44th_Canadian_Federal_\(2021\).csv blue red orange cyan green purple grey
```