all: paper.pdf

# Ensure pandoc is installed
/usr/bin/pandoc:
	sudo apt install -y pandoc

# Ensure LaTeX is installed
/usr/bin/pdflatex:
	sudo apt install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended

# Build the final PDF, ensuring it regenerates if any dependencies change
paper.pdf: paper.tex template.tex /usr/bin/pandoc /usr/bin/pdflatex
	pdflatex paper.tex
	pdflatex paper.tex  # Run twice for proper refs

# Convert Markdown to LaTeX, ensuring it regenerates if any source files or binaries change
paper.tex: index.md template.tex /usr/bin/pandoc
	pandoc index.md -o paper.tex --template=template.tex

# Cleanup intermediate files
clean:
	rm -f paper.aux paper.log paper.out paper.pdf paper.tex
