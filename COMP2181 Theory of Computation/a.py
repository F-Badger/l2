import nbformat

nb1 = nbformat.read("Algorithms and Complexity I.ipynb", as_version=4)
nb2 = nbformat.read("Algorithms and Complexity II.ipynb", as_version=4)

merged = nbformat.v4.new_notebook()
merged.cells = nb1.cells + nb2.cells

nbformat.write(merged, "Algorithms and Complexity.ipynb")