#!/bin/bash

infile=dummy.cgi
outfile=meibo.csv

if [ -e "$infile" ]; then
  nkf -w8 "$infile" > "$outfile"
  sed -i -e "s/\//-/g" "$outfile"
  sed -i -e '1d' "$outfile"
  sed -i '1isimei,simei_kana,email_addr,seibetu,tanjo_bi,blood_gata,chiiki,phone_bango' "$outfile"
  head "$outfile" -n 5
  python ./import.py
fi
