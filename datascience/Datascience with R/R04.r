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

_______________________________________________________

elmat %>%
  sphere_shade(texture = "desert") %>%
  add_water(detect_water(elmat), color = "desert") %>%
  add_shadow(ray_shade(elmat, zscale = 3), 0.5) %>%
  add_shadow(ambient_shade(elmat), 0) %>%
  plot_3d(elmat, zscale = 10, fov = 0, theta = 135, zoom = 0.75, phi = 45, windowsize = c(1000, 800))
Sys.sleep(0.2)
render_snapshot()

__________________________

render_camera(fov = 0, theta = 60, zoom = 0.75, phi = 45)
render_scalebar(limits=c(0, 5, 10),label_unit = "km",position = "W", y=50,
                scale_length = c(0.33,1))
render_compass(position = "E")
render_snapshot(clear=TRUE)

__________________________

elmat %>%
  sphere_shade(texture = "desert") %>%
  add_water(detect_water(elmat), color = "desert") %>%
  plot_3d(elmat, zscale = 10, fov = 0, theta = 60, zoom = 0.75, phi = 45, windowsize = c(1000, 800))

render_scalebar(limits=c(0, 5, 10),label_unit = "km",position = "W", y=50,
                scale_length = c(0.33,1))

render_compass(position = "E")
Sys.sleep(0.2)
render_highquality(samples=200, scale_text_size = 24,clear=TRUE)
render_snapshot(clear=TRUE)


______________________________

## 0) Assainir la session courante (ne PAS décharger le package)
options(rgl.useNULL = FALSE)
Sys.unsetenv("RGL_USE_NULL")   # au cas où il est resté à "true"

## 1) Charger les libs
library(rgl)
library(rayshader)

## 2) Fermer toutes les fenêtres rgl encore ouvertes (sans décharger le package)
if (length(rgl.dev.list())) {
  for (d in rgl.dev.list()) {
    set3d(d)      # activer le device d
    close3d()     # fermer le device courant
  }
}

## 3) Ouvrir une nouvelle fenêtre rgl interactive
if (rgl.cur() == 0) open3d()

## 4) Exemple minimal interactif
elmat <- volcano
elmat %>%
  sphere_shade(texture = "imhof1") %>%
  plot_3d(elmat, zscale = 10, fov = 0, theta = -45, phi = 45,
          windowsize = c(1000, 800))

______________________________

montereybay %>%
  sphere_shade(texture = "desert") %>%
  add_shadow(ray_shade(montereybay,zscale=50)) %>%
  plot_3d(montereybay,water=TRUE, windowsize=c(1000,800), watercolor="dodgerblue")
render_camera(theta=-60,  phi=60, zoom = 0.85, fov=30)

#We will apply a negative buffer to create space between adjacent polygons:
sf::sf_use_s2(FALSE) 
mont_county_buff = sf::st_simplify(sf::st_buffer(monterey_counties_sf,-0.003), dTolerance=0.004)

render_polygons(mont_county_buff,  
                extent = attr(montereybay,"extent"), data_column_top = "ALAND",
                scale_data = 300/(2.6E9), color="chartreuse4",
                parallel=TRUE)
render_highquality(clamp_value=10,samples=256)