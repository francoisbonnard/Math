R.home("bin")
library(jsonlite)
library(languageserver)
library(sf)
5 + 6
a <- 5
b = 6
a == b
name <- c("ad", "ad")
name
mean(c(1, 2, 3))
demo()
help()

# installer une lib
.libPaths("C://Users//franc//OneDrive//Documents//my-projects//Rlib")
install.packages("readxl")
library(readxl)
getwd() # "C:/Users/franc/OneDrive/Documents/vsc/Math"
df <- read_excel("./datascience/testPola.xlsx")
head(df)
str(df)
View(df)

install.packages("readr") # read csv files
library(readr)
Scooby <- read_csv("./datascience/Scooby-Doo Complete - Episode List - Update 10 19 21.csv")
head(Scooby)
View(Scooby)
str(Scooby)
names(Scooby)
sort(names(Scooby))
dim(Scooby)

sink("./datascience/structure_dataset.txt") # Ouvre le fichier et redirige la sortie
str(Scooby) # Ce qui s'affiche normalement dans la console ira dans le fichier
sink() # Ferme la redirection (obligatoire)

mean(Scooby$run.time)

# Sélectionne les colonnes de type integer
scooby_int_cols <- names(Scooby)[sapply(Scooby, is.integer)]
scooby_int_cols <- names(Scooby)[sapply(Scooby, is.numeric)]
sort(scooby_int_cols)

mean(Scooby$imdb, na.rm = TRUE)
class(Scooby$imdb) #character
Scooby$imdb <- as.numeric(Scooby$imdb)
mean(Scooby$imdb, na.rm = TRUE)
class(Scooby$imdb) #numeric


install.packages("tidyverse")
# package 'tidyvese' is not available for this version of R
version
library("tidyverse")

data()
view(mpg)
glimpse(mpg)
? mpg
? mean
? diamonds
? economics
filter(mpg, cty >= 20)
mpg_efficient <- filter(mpg, cty >= 20)
view(mpg_efficient)
mpg_ford <- filter(mpg, manufacturer == "ford")
view(mpg_ford)

mpg_metric <- mutate(mpg, cty_metric = 0.425144 * cty)
glimpse(mpg_metric)

mpg_metric <- mgp %>%
    mutate(cty_metric = 0.425144 * cty)

mpg %>%
    group_by(class) %>%
    summarise(mean(cty))
mpg %>%
    group_by(class) %>%
    summarise(mean(cty), median(cty))

# dataviz with ggplot2 (tidyverse)

ggplot(mpg, aes(x = cty)) +
    geom_histogram() +
        labs(x = "city mileage")

ggplot(mpg, aes(x = cty)) +
    geom_freqpoly() +
        labs(x = "city mileage")

ggplot(mpg, aes(x = cty)) +
    geom_freqpoly() +
    geom_histogram() +
        labs(x = "city mileage")

ggplot(mpg, aes(x = cty, y = hwy)) +
    geom_point() +
        geom_smooth(method = "lm")

ggplot(mpg, aes(x = cty, y = hwy, color = class)) +
    geom_point(size = 3) +
    scale_color_brewer(palette= "Dark2")+
        theme(
             plot.background = element_rect(fill = "black", color = NA),
             panel.background = element_rect(fill = "black"),
             legend.background = element_rect(fill = "black"),
            text = element_text(color = "white", size = 20),
             panel.grid.major = element_line(color = "gray80"),
            panel.grid.minor = element_line(color = "gray40"), # texte global
        )

.libPaths()
