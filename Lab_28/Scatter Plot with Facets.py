from plotnine import *
from plotnine.data import mtcars

p = (
    ggplot(data=mtcars)
    + geom_point(aes("wt", "mpg", color="factor(gear)"))
    + facet_wrap("~gear")
)

print(p)
