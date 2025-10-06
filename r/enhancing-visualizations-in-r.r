library(palmerpenguins)
library(tidyverse)

# Made Vars to shorten the name

p = penguins
flm = p$flipper_length_mm
bm = p$body_mass_g
sp = p$species
sx = p$sex
ggplot(data=p)+geom_point(mapping=aes(x=flm,y=bm, alpha=sx,shape = sp),color="purple")
# size=sp

bl = p$bill_length_mm
bd = p$bill_depth_mm
ggplot(data=p)+geom_point(mapping=aes(x=bl,y=bd))
