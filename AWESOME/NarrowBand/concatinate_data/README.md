# Geomagnetic activity and narrowband data
From matlab tutorial distributed in AWESOME workshop (Tunisia, 2009) by Morris Cohen.

This Python script (concatinate_data.py) allow you to analyze narrowband data from a one-month period during which a large solar flare, and a major geomagnetic storm occurred, along with other changes in geomagnetic activity.

## Result

![Figure](https://github.com/ISWI-Tunisia/AWESOME-SuperSID/blob/master/AWESOME/NarrowBand/concatinate_data/NAALongTermDataKodiak.png)

## What to change in the code?

You may have to change:
* `Rx_name` (line 25)
* `Tx_name` (line 26)
* `pathname` and `filename` values in `ConcatData()` function (line 87)
* `vmin` and `vmax` values (line 95 and line 107)
