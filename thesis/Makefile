#--------------------------------------------------------------------------------
# GNUmakefile to compile ScopingDocument  .tex files through pdflatex
# See README.Howto for usage
#--------------------------------------------------------------------------------
export PATH := /Library/TeX/texbin:$(PATH)

PDFLATEX = pdflatex
BIBTEX   = bibtex
DVIPS    = dvips
LATEXMK  = latexmk
DIFF     = master --

VPATH =$(shell ls)
Sources = $(shell find ./ -name [A-z]\*.tex| xargs)
Styles = $(shell find ./ -name [A-z]\*.sty| xargs)
Classes = $(shell find ./ -name [A-z]\*.cls| xargs)
EPSFigures = $(shell find . -name *.eps | xargs)
PDFFigures = $(shell find . -name *.pdf | xargs)
# PDFFigures = $(patsubst %.eps, %.pdf, ${EPSFigures})

BASENAME  = thesis_dantrim
DRAFT   = $(BASENAME)

PROG	= $(BASENAME)
PROGALT	= $(BASENAME)

SRCS	= $(wildcard ./*.tex ./*/*.tex ./*/*/*.tex )
FIGS	= $(wildcard ./figures/*.* ./*/figures/*.* ./*/*/figures/*.*)


default: $(DRAFT)
alt: $(DRAFT)_alt

$(PROG):	$(PROG).pdf

$(DRAFT):	$(DRAFT).pdf

$(DRAFT)_alt:	$(DRAFT)_alt.pdf

APP     = $(DRAFT)_Appendices


nobib:
	$(LATEXMK) -nobibtex -pdf -use-make $(DRAFT)

clean:
	rm -rf $(PROG).pdf $(DRAFT)*.pdf *_synopsis.pdf
	$(LATEXMK) -C
	rm -rf latexdiff
	find . -type f \( -iname "*.aux" -o -iname "*.log" -o -iname "*.bbl" -o -iname "*.dvi" -o -iname "*.bbl" -o -iname "*.blg" -o -iname "*.brf" -o -iname "*.cb" -o -iname "*.ind" -o -iname "*.ilg" -o -iname "*.inx" -o -iname "*.toc" -o -iname "*.out" -o -iname "*~" -o -iname "*.synctex.gz" -o -iname "*.lot" -o -iname "*.maf" -o -iname "*.mtc*" -o -iname "*.gls" -o -iname "*.glsdefs" -o -iname "*.glo" -o -iname "*.ist" -o -iname "*.glg" -o -iname "*.lof" -o -iname "*.not" -o -iname "*.nlg" -o -iname "*.mw" -o -iname "*.lor*" -o -iname "*.lod*" -o -iname "*.tks" -o -iname "*.txss" -o -iname "*.ver" -o -iname "*.hst" -o -iname "*.tmp" -o -iname "*.tui" -o -iname "*.mp" -o -iname "*.bak" -o -iname "*-blx.bib" -o -iname "*.run.xml" -o -iname "*.fls" \) -exec rm {} \;


cleanpdf:
	rm -f $(PROG).pdf $(DRAFT).pdf $(DRAFT)_alt.pdf

app:    $(APP).pdf

full:	$(PROG)

draft:	$(DRAFT)

%.pdf:	%.tex $(Classes) $(Styles) $(Sources)
	@echo Compiling $*
	$(LATEXMK) -r latexmkrc -e "$$max_repeat 5" -f -bibtex -pdf -use-make $*

$(DRAFT)_alt.pdf: $(DRAFT)_alt.tex  $(Classes) $(Styles) $(Sources)
	@echo Compiling $<
	$(LATEXMK) -r latexmkrc_alt -e "$$max_repeat 5" -diagnostics -f -bibtex -pdf -use-make $(DRAFT)_alt

#snapshot: $(DRAFT).pdf 
#	@- $(foreach file, $^, \
#		$(MAKE) $(file); \
#		cp $(file) $(file:.pdf=)_`date +'%d%m%Y'`_`date +'%H%M'`.pdf;\
#	)

snapshot: $(DRAFT).pdf 
	@- $(foreach file, $^, \
		cp $(file) $(file:.pdf=)_`date +'%d%m%Y'`_`date +'%H%M'`.pdf;\
	)

# make diff
# make diff DIFF="master mybranch"
# default is using 'HEAD~1'

diff:
	mkdir -p latexdiff
	rm -rf latexdiff/*
	git-latexdiff $(DIFF) --main $(DRAFT).tex --tmpdirprefix latexdiff --latexmk --no-view
	mv latexdiff/git-latexdiff.*/$(DRAFT).pdf $(DRAFT)_diff.pdf
	rm -rf latexdiff




