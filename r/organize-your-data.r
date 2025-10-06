library(palmerpenguins)
library(tidyverse)

p = penguins
pBillAsec = p %>% arrange(bill_length_mm)
pBillDesec = p %>% arrange(-bill_length_mm)
# After making a function, assign it to a var, to save it.

# drop_na drops all Nulls
BillMean = p %>% group_by(island) %>% drop_na() %>% summarize(mean_bill_length = mean(bill_length_mm))
BillMax = p %>% group_by(island) %>% drop_na() %>% summarize(max_bill_length = max(bill_length_mm))

BillSpec = p %>% group_by(species, island) %>% drop_na() %>% summarize(mean_bill = mean(bill_length_mm), max_bill = (max(bill_length_mm)))

pAdelie = p %>% filter(species == "Adelie")
