library(here)
library(skimr)
library(janitor)
library(tidyverse)

#read_csv(filename) for your data

library(palmerpenguins)
p = penguins
skim_without_charts(p)
glimpse(p)
head(p)
ps = p %>%  select(species) # select only
print(ps)
p_s = p %>% select(-species) # select without
print(p_s)
# p %>% rename(island_new=island) renames a col
rename_with(p, tolower) # changes the case

clean_names(p)
# checks for viable names