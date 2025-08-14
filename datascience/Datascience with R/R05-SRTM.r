library(terra)

install.packages("geodata")
library(geodata)

# Emprise en lon/lat (WGS84) ~ Bassin parisien
ext_paris <- ext(1.0, 4.5, 47.5, 50.0)

# Coordonnées approximatives du centre du Bassin parisien
lon <- 2.5
lat <- 48.8


# Télécharge la tuile SRTM 90m autour du point
mnt <- geodata::elevation_3s(lon = lon, lat = lat, path = tempdir())
plot(mnt)

# 2. Conversion en matrice pour rayshader
elmat <- raster_to_matrix(raster::raster(mnt))

# 3. Rendu 3D interactif
elmat |>
  sphere_shade(texture = "imhof1") |>
  plot_3d(elmat, zscale = 50, fov = 0, theta = 135, phi = 45, windowsize = c(1000, 800))

