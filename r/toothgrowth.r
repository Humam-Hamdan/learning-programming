library(tidyverse)
data(ToothGrowth)
# View(ToothGrowth)

x = ToothGrowth

filtered_tg = filter(x, dose==0.5)
# View(filtered_tg)

arrange(filtered_tg, len)

arrange(filter(x, dose>0.5), len)

filtered_toothgrowth = ToothGrowth %>% 
  filter(dose<=0.5) %>% 
  arrange(len)
View(filtered_toothgrowth)

filtered_toothgrowt = ToothGrowth %>% 
  filter(dose<=0.5) %>% 
  group_by(supp) %>% 
  summarise(mean_len = mean(len,na.rm = T)) %>% 
  arrange(len)
View(filtered_toothgrowt)
