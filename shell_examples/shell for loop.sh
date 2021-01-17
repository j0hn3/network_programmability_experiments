for dir in /tmp/*/     # list directories in the form "/tmp/dirname/"
do
    dir=${dir%*/}      # remove the trailing "/"
    echo ${dir##*/}    # print everything after the final "/"
done

Ref: https://stackoverflow.com/questions/2107945/how-to-loop-over-directories-in-linux