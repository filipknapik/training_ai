#!/bin/sh

cd
cd Documents/aiworkshop
current_dir=$(pwd)

case "$current_dir" in
  *aiworkshop)
    mv training_ai training_ai_old
    git clone https://github.com/filipknapik/training_ai.git
    cp training_ai_old/envvars.sh training_ai/envvars.sh
    ;;
  *)
    echo "The current directory ($current_dir) does not end in 'abc'."
    ;;
esac