# https://www.rayshader.com/
#.libPaths("C://Users//franc//OneDrive//Documents//my-projects//Rlib")
.libPaths(file.path("C:", "Users", "franc", "OneDrive", "Documents", "my-projects", "Rlib"))

install.packages("devtools")
library(devtools)

# https://cran.r-project.org/bin/windows/Rtools/rtools45/rtools.html

devtools::install_github("tylermorganwall/rayshader")

library(rayshader)

dir.create("C:/Rlib", showWarnings = FALSE)
setwd("C:/Rlib")
.libPaths("C:/Rlib")

install.packages("devtools")       # si pas encore installé
library(devtools)
devtools::install_github("tylermorganwall/rayshader")

version

# next step https://www.youtube.com/watch?v=N-AtAnXrGm0