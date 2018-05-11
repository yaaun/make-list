# make-list
Generates a peculiarly&hyphen;formatted list from a particular type of CSV.

## Input syntax
The input file format resembles tab&hyphen;separated CSV (or TSV) with a few adaptations:

### The number of columns makes a difference
Lines (rows) are interpreted differently depending on how many columns are supplied.

Column count | Interpretation
-----------: |---------------
1            | Category name
2            | 

### Comments
Line comments/line ignoring are enabled by inputting a hash symbol (U+0023) at the beginning of the line:
    # This is a comment and will not produce output.
Though this has the downside of not allowing the hash symbol in the first column, who in their right mind would want to put one there?
