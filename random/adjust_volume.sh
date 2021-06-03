while (( 1 ))
do
    VOLUME=`osascript -e "input volume of (get volume settings)"`
    if (( $VOLUME != 25 ))
    then
        osascript -e "set volume input volume (25)"
    fi
done
