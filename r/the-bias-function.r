library(SimDesign)
actual_temp = c(68.3,70,72.4,71,67,70)
predictions = c(67.9,69,71.5,70,67,69)
bias(actual_temp,predictions)

actual_sales = c(150,203,137,247,116,287)
predict_sales = c(200,300,150,250,150,300)
bias(actual_sales,predict_sales)
