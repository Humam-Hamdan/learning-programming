library(palmerpenguins)
library(tidyverse)

# Made Vars to shorten the name

d = diamonds
p = penguins
flm = p$flipper_length_mm
bm = p$body_mass_g
sp = p$species
sx = p$sex
bl = p$bill_length_mm
bd = p$bill_depth_mm

ggplot(data=p)+geom_point(mapping=aes(x=flm,y=bm))
ggplot(data=p)+geom_smooth(mapping=aes(x=flm,y=bm))
ggplot(data=p)+geom_bar(mapping=aes(x=sp))
ggplot(data=p)+geom_line(mapping=aes(x=flm,y=bm))
ggplot(data=p)+geom_point(mapping=aes(x=flm,y=bm))+
  geom_smooth(mapping=aes(x=flm,y=bm, linetype=sp))
ggplot(data=p)+geom_jitter(mapping=aes(x=flm,y=bm,color=sp))

ggplot(data=d)+
  geom_bar(mapping=aes(y=cut,fill=clarity)) # x for vertical chart
# fill = fill color / color outside


