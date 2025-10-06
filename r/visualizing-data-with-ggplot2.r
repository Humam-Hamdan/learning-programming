library(tidyverse)
library(palmerpenguins)
p = penguins

ggplot(data = penguins) + geom_point(
  mapping = aes(x = flipper_length_mm, y = body_mass_g)
  )

ggplot(data = penguins, mapping = aes(
  x = flipper_length_mm, y = body_mass_g)) +  geom_point()