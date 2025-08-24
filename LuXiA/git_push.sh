#!/bin/bash

echo "Escribe el mensaje para el commit:"
read commit_message

git add .
git commit -m "$commit_message"
git push origin main
