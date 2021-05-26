while (( `osascript -e "input volume of (get volume settings)"` != 25 ))
do
    VOLUME=`osascript -e "input volume of (get volume settings)"`
    if (( $VOLUME < 25 ))
    then
        osascript -e "set volume input volume ($VOLUME + 1)"
    fi
    if  (( $VOLUME > 25 ))
    then
        osascript -e "set volume input volume ($VOLUME - 1)"
    fi
    sleep 0.0025
done
