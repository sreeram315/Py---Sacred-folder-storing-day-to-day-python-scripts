# Calculating the relation ship between previous marks of the student to 
# his attendance.
# And know whether students attending more classes are having better marks
# and vice-versa

df = read.csv("/Users/sreerammaram/Downloads/CA.csv", header = TRUE)
#View(dataset)
#s = sample(20000, 7123)
#split = sample.split(df$X1, SplitRatio = 9/10)

df$avg_att = (df$CurrentAttendance + df$LastAttendance + df$SecondLastAttendance)/3
n = nrow(df)
split = sample(c(TRUE, FALSE), n, replace=TRUE, prob=c(0.88, 0.12))



#data_norm <- function(x){((x-min(x))/(max(x)-min(x)))}
#df_norm   <- as.data.frame(lapply(df[-10], data_norm))
df = df[-1]
df = df[-7]
df <- df[order(df$OverallMarks), ]
plot(df$OverallMarks, df$avg_att, type = "o")

train_df  <-   df[split, ]
test_df   <-   df[!split, ]

df_pred  <-  knn(train_df, test_df, df[split, 8], k = 5)


table(df_pred, test_df[10])

plot(df_pred)
plot(df[!split, 10])





