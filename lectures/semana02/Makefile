TEXS = semana02-P1.tex semana02-P2.tex
PDFS = $(TEXS:.tex=.pdf)
BUILD = build
TMP = tmp
AUX_EXT = aux log out toc lof lot fls fdb_latexmk synctex.gz nav snm vrb

.PHONY: pdf clean distclean

pdf: $(PDFS)

%.pdf: %.tex preamble.tex
	mkdir -p $(BUILD) $(TMP)/texmf-var
	env TEXMFVAR=$(CURDIR)/$(TMP)/texmf-var TEXMFCACHE=$(CURDIR)/$(TMP)/texmf-var \
		lualatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $<
	env TEXMFVAR=$(CURDIR)/$(TMP)/texmf-var TEXMFCACHE=$(CURDIR)/$(TMP)/texmf-var \
		lualatex -interaction=nonstopmode -halt-on-error -output-directory=$(BUILD) $<
	cp $(BUILD)/$@ .

clean:
	rm -rf $(BUILD) $(TMP)
	for ext in $(AUX_EXT); do rm -f *.$$ext; done

distclean: clean
	rm -f $(PDFS)
