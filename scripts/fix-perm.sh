#!/usr/bin/env bash

set -e

for d in "$@"; do
    find "${d}" \
        ! \( \
            -group "${NB_GID}" \
            -a -perm -g+rwX \
        \) \
        -exec chgrp "${NB_GID}" {} \; \
        -exec chmod g+rwX {} \;
    # setuid, setgid *on directories only*
    find "${d}" \
        \( \
            -type d \
            -a ! -perm -6000 \
        \) \
        -exec chmod +6000 {} \;
done