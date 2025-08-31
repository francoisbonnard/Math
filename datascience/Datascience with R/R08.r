install.packages("languageserver")
library(languageserver)


install.packages("tidyverse")
library(tidyverse)

# ── Conflicts ───────────────────────────────────────────────────────── tidyverse_conflicts() ──
# ✖ dplyr::filter() masks stats::filter()
# ✖ dplyr::lag()    masks stats::lag()

install.packages("conflicted")
library(conflicted)
conflict_prefer("filter", "dplyr")
conflict_prefer("lag", "dplyr")
# ou l’inverse selon ton usage :
# conflict_prefer("filter", "stats")

install.packages("palmerpenguins")
library(palmerpenguins)
install.packages("ggthemes")
library(ggthemes)

penguins
glimpse(penguins)
view(penguins)

ggplot(data=penguins)

ggplot(
data = penguins,
mapping = aes(x = flipper_length_mm, y = body_mass_g)
) + geom_point() +geom_smooth(method = "lm")

ggplot(
data = penguins,
mapping = aes(x = flipper_length_mm, y = body_mass_g)
) + geom_point(mapping=aes(color=species, shape=species)) +geom_smooth(method = "lm")

ggplot(
data = penguins,
mapping = aes(x = flipper_length_mm, y = body_mass_g)
) +
geom_point(aes(color = species, shape = species)) +
geom_smooth(method = "lm") +
labs(
title = "Body mass and flipper length",
subtitle = "Dimensions for Adelie, Chinstrap, and Gentoo Penguins",
x = "Flipper length (mm)", y = "Body mass (g)",
color = "Species", shape = "Species"
) +
scale_color_colorblind()

ggplot(penguins, aes(x = flipper_length_mm, y = body_mass_g)) +
geom_point()

penguins |>
ggplot(aes(x = flipper_length_mm, y = body_mass_g)) +
geom_point()

ggplot(penguins, aes(x = species)) +
geom_bar()

ggplot(penguins, aes(x = fct_infreq(species))) +
geom_bar()

ggplot(penguins, aes(x = body_mass_g)) +
geom_histogram(binwidth = 50)

ggplot(penguins, aes(x = body_mass_g)) +
geom_density()

theme_set(theme_minimal(base_size = 30))
theme_update(
  plot.title = element_text(size = 20, face = "bold"),
  axis.title = element_text(size = 14),
  axis.text  = element_text(size = 12),
  legend.title = element_text(size = 13),
  legend.text  = element_text(size = 11),
  strip.text   = element_text(size = 13)
)

ggplot(penguins, aes(x = species)) +
geom_bar(color = "red", fill ="white")
ggplot(penguins, aes(x = species)) +
geom_bar(fill = "red")

diamonds
glimpse(diamonds)

ggplot(diamonds, aes(x = carat)) +
geom_bar(color = "red", fill ="#52c515")

ggplot(diamonds, aes(x = carat)) +
geom_histogram(binwidth = 0.1)

utils::data(package = "ggplot2")
utils::data(package = "datasets")

ds_g <- as.data.frame(utils::data(package = "ggplot2")$results, stringsAsFactors = FALSE)
ds_g

ggplot(penguins, aes(x = species, y = body_mass_g)) +
geom_boxplot() 

ggplot(penguins, aes(x = body_mass_g, color = species)) +
geom_density(linewidth = 0.75)
ggplot(penguins, aes(x = body_mass_g, color = species, fill=species)) +
geom_density(alpha = 0.3)

ggplot(penguins, aes(x = island, fill = species)) +
geom_bar()

# Ouvre la recherche OEIS dans ton navigateur avec tes termes
oeis_open <- function(terms) {
  q <- paste(terms, collapse = ",")
  utils::browseURL(sprintf("https://oeis.org/search?q=%s&sort=score&fmt=html",
                           utils::URLencode(q, reserved = TRUE)))
}
# Exemple :
oeis_open(c(1,1,2,3,5,8,13))  # Fibonacci (A000045)
