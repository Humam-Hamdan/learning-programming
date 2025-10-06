# importing library
library(tidyverse)
# importing data
tripsq <- read.csv("Divvy_Trips_2020_Q1.csv")
# vers names
colnames(tripsq)
# viewing dataset
view(tripsq)
# filtering members and casuals
membercasual <- filter(tripsq,member_casual == "casual")
membermember <- filter(tripsq, member_casual == "member")
# checking data formatting
glimpse(tripsq)
# started at - ended at = are formatted wrongly.
# changing the datatype for the cols
