id <- c(1:10)

name <- c("John Mendes", "Rob Stewart", "Rachel Abrahamson", 
          "Christy Hickman", "Johnson Harper", "Candace Miller", 
          "Carlson Landy", "Pansy Jordan", "Darius Berry", "Claudia Garcia")

job_title <- c("Professional", "Programmer", "Management", "Clerical", 
               "Developer", "Programmer", "Management", "Clerical", 
               "Developer", "Programmer")

employee <- data.frame(id, name, job_title)
e = employee  

print(employee)

es = separate(e, name, into=c("FirstName","LastName"), sep=" ")
esu = unite(es, "name", FirstName, LastName, sep=" ") 

p = penguins
pMutate = p %>% mutate(bodymassKG=body_mass_g/1000, flipperM = flipper_length_mm/1000)
