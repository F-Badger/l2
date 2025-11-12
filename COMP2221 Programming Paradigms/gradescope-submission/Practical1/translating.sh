cat legacy_inventory.dat | tr "\t" "," | tr -d "!@$%#*" | nl -s "" |  tr "A-Z" "a-z"
