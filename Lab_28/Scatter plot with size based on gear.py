from plotnine import *
from plotnine.data import mtcars

(
    ggplot(data=mtcars)
    + geom_point(aes("wt", "mpg", size="factor(gear)"))
)
