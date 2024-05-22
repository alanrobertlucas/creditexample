# Test Program

import polars as pl

cr='\n'
q = (
    pl.scan_csv("iris.csv")
    .filter(pl.col("sepal.length") > 5)
    .group_by("variety")
    .agg(pl.all().sum())
)

df = q.collect()
print(cr,df,cr)

