# You have 137 passengers booked on a flight from Las Vegas to Dallas. However, it
# is Las Vegas on a Sunday morning and you estimate each passenger is 40% likely
# to not show up.
# You are trying to figure out how many seats to overbook so the plane does not fly
# empty.
# How likely is it at least 50 passengers will not show up?

.libPaths("C:/Rlib")
install.packages("tidyverse")
library(tidyverse)

# Paramètres
n <- 137
p <- 0.40
x <- 0:n # crée un vecteur de 0 à n
y <- dbinom(x, n, p)

p_50_or_more <- 1 - pbinom(49, n, p)
cat("Probabilité d’avoir au moins 50 absents :", round(p_50_or_more * 100, 2), "%\n")

# Data frame
df <- data.frame(x = x, y = y, highlight = x >= 50)
view(df)
# Tracé
ggplot(df, aes(x = x, y = y, fill = highlight)) +
  geom_col(show.legend = FALSE) +
  scale_fill_manual(values = c("TRUE" = "red", "FALSE" = "lightgray")) +
  geom_vline(xintercept = 50, linetype = "dashed", color = "black") +
  labs(
    title = "Distribution binomiale : P(X ≥ 50) avec n=137, p=0.40",
    x = "Nombre de passagers absents (X)",
    y = "Probabilité"
  ) +
  theme_minimal()
