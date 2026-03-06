# 1. Chargement des bibliotheques
library(corrplot)
library(dplyr)

# 2. Chargement du fichier
df <- read.csv('C:/Users/remyg/Documents/water_quality/data/water_potability.csv')

# 3. Selection des colonnes
df_subset <- df[, c('ph', 'Sulfate', 'Chloramines', 'Hardness', 'Potability')]

# 4. Suppression des lignes avec des cases vides (NA)
df_clean <- na.omit(df_subset)

# 5. Calcul de la matrice
cor_matrix <- cor(df_clean)

# 6. Affichage du graphique
pearson_matrix <- cor(df_clean, method = "pearson")

corrplot(pearson_matrix, 
         method = "number",
         type = "upper",
         tl.col = "black",
         col = COL2('RdBu'),  
         title = "Matrice de Pearson (Corrélations Linéaires)",
         mar = c(0,0,1,0))
