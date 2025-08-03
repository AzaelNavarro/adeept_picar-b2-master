#!/bin/bash

# Pregunta al usuario el mensaje del commit
echo "Escribe el mensaje para el commit:"
read commit_message

# Añade todos los cambios
git add .

# Hace el commit con el mensaje que pusiste
git commit -m "$commit_message"

# Empuja los cambios a GitHub
git push
