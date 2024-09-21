#!/bin/sh

for d in log/????; do
    grep '^\* ' $d/index.md | \
        grep ' - ' |
	grep -vP '📝|⚠️|💡|💩|📽️|🖼️' |
	perl -pe "s#\]\((?!http|/)#]($d/#g"
done | sort -r
