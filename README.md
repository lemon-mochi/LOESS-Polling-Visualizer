To run
```
python3 plotter.py <csv file with polling data> <OPTIONAL: Colour for candidate/party 1> <OPTIONAL: Colour for candidate/party 2> <OPTIONAL: Colour for candidate/party 3> ...
```

## Libraries needed
Pandas, statsmodel, matplotlib, colour

## Other
Data containing the polls should already be sorted. The program will randomly generate a colour if the user does not specify a colour in the command line or if python cannot understand the colour that was given. For example, if the user types `adlfkjdkflj` as a colour, the program ignores it and generates a random colour.