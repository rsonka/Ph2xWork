# Makefile for Ph 20 week 3 assignment-done as part of week 4 assignment.
# Graphics Files
GF = week3Graphics/
# Graphics Generation
GG = plotGenerationScripts/


week3report.pdf : week3report.tex $(GG)*
	pdflatex $^

$(GG)%.py : 
	python $@ $(GF)



