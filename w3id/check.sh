#!/usr/bin/env bash
# Check that the w3id redirects resolve, once the pull request is merged.
#
#   bash w3id/check.sh
#
# Every IRI is asked twice: once as a browser would, once as a reasoner
# would. Both must answer 303 and point at a page that exists.

set -u
W3ID=https://w3id.org/aias
fail=0

ask() {           # ask <iri> <accept> <what>
    local out code loc
    out=$(curl -sI -H "Accept: $2" "$1")
    code=$(printf '%s' "$out" | head -1 | tr -d '\r' | cut -d' ' -f2)
    loc=$(printf '%s' "$out" | tr -d '\r' | grep -i '^location:' | cut -d' ' -f2-)

    if [ "$code" != "303" ]; then
        printf '  FAIL  %-34s %-6s HTTP %s\n' "$1" "$3" "${code:-none}"
        fail=1
        return
    fi

    # The target has to exist as well: a 303 to a 404 helps nobody.
    local tcode
    tcode=$(curl -s -o /dev/null -w '%{http_code}' "$loc")
    if [ "$tcode" != "200" ]; then
        printf '  FAIL  %-34s %-6s -> %s (HTTP %s)\n' "$1" "$3" "$loc" "$tcode"
        fail=1
        return
    fi

    printf '  ok    %-34s %-6s -> %s\n' "$1" "$3" "${loc#https://schiesem.github.io/aias/}"
}

check() {         # check <iri>
    ask "$1" "text/html"   "html"
    ask "$1" "text/turtle" "ttl"
}

echo "Alignment"
check "$W3ID"
check "$W3ID/1.0.0"
check "$W3ID/2.0.0"

echo
echo "Patterns, current version"
for p in vdi3682 iso7498 iso22989 iec60050; do
    check "$W3ID/odp/$p"
done

echo
echo "Patterns, explicit version"
for p in vdi3682 iso7498 iso22989; do
    check "$W3ID/odp/$p/1.0.0"
    check "$W3ID/odp/$p/2.0.0"
done
check "$W3ID/odp/iec60050/1.0.0"

echo
if [ $fail -eq 0 ]; then
    echo "Every IRI resolves."
else
    echo "Something does not resolve. If the pull request is not merged yet,"
    echo "that is expected: w3id answers 404 until it is."
    exit 1
fi
