#!/bin/sh

clean_on_exit () {
    test -n "$MEMCACHED_DIR" && rm -rf "$MEMCACHED_DIR"
}

trap clean_on_exit EXIT

wait_for_line () {
    while read line
    do
        echo "$line" | grep -q "$1" && break
    done < "$2"
    # 작업이 블록 되지 않도록, 계속 대기열을 읽어준다.
    cat "$2" >/dev/null &
}

MEMCACHED_DIR=`mktemp -d`
mkfifo ${MEMCACHED_DIR}/out
memcached -p 4526 -vv > ${MEMCACHED_DIR}/out 2>&1 &
export MEMCACHED_PID=$!
wait_for_line "server listening" ${MEMCACHED_DIR}/out

$*

kill ${MEMCACHED_PID}