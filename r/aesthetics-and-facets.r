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

ggplot(data=penguins %>% drop_na())+
  geom_point(mapping = aes(x=flipper_length_mm ,y=body_mass_g, color=species))+
  facet_grid(sex~species)  
# facet_wrap(sp)
# Why didn't it take the var? tibble vs dframe?

ggplot(data=diamonds)+
  geom_bar(mapping=aes(x=cut,fill=cut)) +facet_wrap(cut)

