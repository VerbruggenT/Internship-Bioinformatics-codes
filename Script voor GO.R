## try http:// if https:// URLs are not supported
source("https://bioconductor.org/biocLite.R")
biocLite("BridgeDbR")

# De libary wordt geopend van de volgende tools:

library("rJava", lib.loc="~/R/win-library/3.4")
library("RCurl", lib.loc="~/R/win-library/3.4")
library("devtools", lib.loc="~/R/win-library/3.4")
library("BridgeDbR", lib.loc="~/R/win-library/3.4")


mbmaps = loadDatabase("C:/Users/timme/Documents/R/Hs_Derby_Ensembl_91.bridge/Hs_Derby_Ensembl_91.bridge")
setwd("C:/Users/timme/Documents/R")


# lijst met GO wordt geopend.

LijstmetGOs <- read.table("~/R/LijstmetGOtim(6).txt", quote="\"", comment.char="")


helper = function(x) {
  result = map(mbmaps, "T", x, "En")
  
  return(result)
}

Ensemble = unlist(sapply(as.character(LijstmetGOs[,1]), helper))
data2 = cbind(c(Ensemble,""))



write.table(data2, "List of Ensemble Identifiers Tim(6).txt", sep="\t")  



