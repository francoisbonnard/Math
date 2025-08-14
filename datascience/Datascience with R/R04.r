library(jsonlite)
library(languageserver)
library(sf)
library(readxl)

getwd() # "C:/Users/franc/OneDrive/Documents/vsc/Math"
df <- read_excel("./datascience/Datascience with R/testPola.xlsx")
head(df)

installed.packages()[, "Package"]
library(usethis)
library(devtools)

devtools::install_github("tylermorganwall/rayshader")

library(rayshader)

#Here, I load a map with the raster package.
loadzip = tempfile() 
download.file("https://tylermw.com/data/dem_01.tif.zip", loadzip)
localtif = raster::raster(unzip(loadzip, "dem_01.tif"))
unlink(loadzip)

#And convert it to a matrix:
elmat = raster_to_matrix(localtif)

#We use another one of rayshader's built-in textures:
elmat %>%
  sphere_shade(texture = "desert") %>%
  plot_map()

montereybay %>%
  sphere_shade(texture = "desert") %>%
  add_shadow(ray_shade(montereybay,zscale=50)) %>%
  plot_3d(montereybay,water=TRUE, windowsize=c(1000,800), watercolor="dodgerblue")
render_camera(theta=-60,  phi=60, zoom = 0.85, fov=30)

plot_map(sphere_shade(montereybay))

data(package = "rayshader")$results[, "Item"]

install.packages("elevatr")
install.packages("terra")

library(sf)
library(elevatr)
library(rayshader)


# 1) Construis un sf (pas juste un sfc/bbox)
bb <- st_bbox(c(xmin = 1.0, ymin = 47.5, xmax = 4.5, ymax = 50.0), crs = st_crs(4326))
emprise <- st_as_sfc(bb)                 # sfc
emprise <- st_sf(id = 1, geometry = emprise)  # <-- sf avec 1 ligne

# 2) (Optionnel si proxy Windows) aide les téléchargements
options(download.file.method = "wininet")

# 3) Télécharge en découpant sur la bbox (plus robuste)
mnt <- get_elev_raster(emprise, z = 8, prj = "EPSG:4326", clip = "bbox")

# rayshader
elmat <- raster_to_matrix(mnt)
elmat |> sphere_shade() |> plot_map()
# 3D :
elmat |> sphere_shade() |> plot_3d(elmat,water=TRUE, watercolor="dodgerblue", zscale = 50)
elmat |> sphere_shade() |> plot_3d(elmat,water=TRUE, zscale = 10)

  plot_3d(montereybay,water=TRUE, windowsize=c(1000,800), watercolor="dodgerblue")
_________________________________________________

# Geodatalibrary(terra)
library(geodata)  # installez-le si besoin

# Emprise
ext <- ext(1.0, 4.5, 47.5, 50.0)

# SRTM 30 m (1s) si dispo, sinon 90 m (3s)
srtm <- geodata::elevation_1s(ext = ext, path = tempdir())  # remplacez par elevation_3s() si 1s indispo

# Vers rayshader
library(rayshader)
# convertir SpatRaster -> RasterLayer si nécessaire
elmat <- raster_to_matrix(raster::raster(srtm))
elmat |> sphere_shade() |> plot_map()


library(terra)
library(geodata)  # installez-le si besoin

# Emprise
ext <- ext(1.0, 4.5, 47.5, 50.0)

# SRTM 30 m (1s) si dispo, sinon 90 m (3s)
srtm <- geodata::elevation_1s(ext = ext, path = tempdir())  # remplacez par elevation_3s() si 1s indispo

# Vers rayshader
library(rayshader)
# convertir SpatRaster -> RasterLayer si nécessaire
elmat <- raster_to_matrix(raster::raster(srtm))
elmat |> sphere_shade() |> plot_map()

__________________________________________________

library(terra)
# liste de fichiers .tif téléchargés
files <- list.files("C:/chemin/IGN_RGE_ALTI/", pattern = "\\.tif$", full.names = TRUE)
mnt_ign <- mosaic(rast(files))
# recadrage éventuel :
mnt_ign <- crop(mnt_ign, ext(1.0, 4.5, 47.5, 50.0))
library(rayshader)
elmat <- raster_to_matrix(raster::raster(mnt_ign))
elmat |> sphere_shade() |> plot_map()
