#! /bin/bash
cat top.html>børn.html
for f in *.data
do
echo "<div class=\"one-third column\" >">>børn.html
echo "##${f%.*}">børn.md
sort $f >> børn.md

pandoc børn.md -t html >>børn.html
wc -l $f >> børn.html
echo "</div>">>børn.html

done
cat bottom.html>>børn.html
