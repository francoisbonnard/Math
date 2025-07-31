[tuto](https://www.youtube.com/watch?v=k79H8EeR5Jo)

download from this [link](https://cran.r-project.org/bin/windows/base/)

Copy this path : C:\Program Files\R\R-4.5.1\library

Make env variables : R_LIBS_USER with this value : C:\Program Files\R\R-4.5.1\library

In this folder : C:\Program Files\R\R-4.5.1\bin\x64

run in admin mode : Rgui

type :

 install.packages("languageserversetup")
 install.packages("languageserver")
 languageserversetup::languageserver_install()
 languageserversetup::languageserver_add_to_rprofile()

In VSC : add R extension 

New File : R document
New R Terminal
type in the file : R.home("bin")
Select this and alt+enter

copy the result in the terminal : C:/PROGRA~1/R/R-45~1.1/bin/x64"
Go back to the extension / click manage / extension settings
Find : Rpath Windows 

Return in the RGUI and type : install.packages("sf")

now in the VSC File : library(sf)

To avoid the error : 

RGUI : install.packages("jsonlite")
VSC : library(jsonlite) 

ctrl , -> 
R_term_win : C:\Program Files\R\R-4.5.1\bin
r.lsp.args": ["--slave", "-e", "languageserver::run()"]

.libPaths("C:\Users\franc\OneDrive\Documents\my-projects\Rlib")


