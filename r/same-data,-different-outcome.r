library(Tmisc)

q = quartet
view(q)

q %>% 
  group_by(set) %>% 
  summarise(mean(x),sd(x),mean(y),sd(y),cor(x,y))
# mean / standart deviation / correlation

library(tidyverse)

library(datasauRus)

# made Viz in the vid.
ggplot(datasaurus_dozen,aes(x=x,y=y,colour=dataset)
       )+geom_point()+theme_void()+theme(legend.position = "none"
                                         )+facet_wrap(~dataset,ncol=3) 

# Explore the data in multi ways