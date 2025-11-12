cat legacy_inventory.dat | tr "\t" "," | tr "!@$%" "1234" |  tr "A-Z" "a-z"
