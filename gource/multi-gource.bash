#!/bin/bash

function multi() {
    mkdir /tmp/multi-gource
    mkdir /tmp/multi-gource/user-image-dir
    export CODE="$PWD"
    cd "$1"
    shift
    find . -type d -name ".git" | while read dir
    do
        CUT1=${dir#./}
        export SUBDIR=${CUT1%/.git}
        sh -c "$*"
    done
    cat /tmp/multi-gource/*.txt | sort -n > /tmp/multi-gource/combined.txt
    gource --auto-skip-seconds 1 --user-image-dir /tmp/multi-gource/user-image-dir /tmp/multi-gource/combined.txt -s 1
    rm /tmp/multi-gource/user-image-dir/*
    rmdir /tmp/multi-gource/user-image-dir
    rm /tmp/multi-gource/*
    rmdir /tmp/multi-gource
}

function run_gsource() {
    cd $SUBDIR
    $CODE/gource-gravatar.perl
    cd -
    logfile="$(mktemp /tmp/multi-gource/log.XXXX.txt)"
    cp $SUBDIR/.git/avatar/* /tmp/multi-gource/user-image-dir
    gource --output-custom-log $logfile $SUBDIR
    sed -i -r "s#(.+)\|#\1|/$SUBDIR#" $logfile
}

export -f run_gsource
multi $1 run_gsource
