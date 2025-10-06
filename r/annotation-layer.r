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
  labs(title = "flm vs bm!", subtitle = "i'm a sub, horra!", caption = "collected by Gorman")+
  annotate("text",x=220,y=3500,label="Gentoo Lage OOO!",color="Red", fontface="italic", size=4,angle=45)

p2=ggplot(data=penguins)

p2+   
  geom_point(mapping = aes(x=flipper_length_mm ,y=body_mass_g, color=species))+
  labs(title = "flm vs bm!", subtitle = "i'm a sub, horra!", caption = "collected by Gorman")+
  annotate("text",x=220,y=3500,label="Gentoo Lage OOO!",color="Red", fontface="italic", size=4,angle=45)


# Why didn't it take the var? tibble vs dframe?
