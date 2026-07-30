ENGINE ?= lualatex
SOURCE = presentacion.tex
TARGET = presentacion-experiencia01.pdf
BUILD = build

.PHONY: pdf clean

pdf:
	mkdir -p $(BUILD)
	latexmk -$(ENGINE) -interaction=nonstopmode -halt-on-error -outdir=$(BUILD) $(SOURCE)
	cp $(BUILD)/presentacion.pdf $(TARGET)

clean:
	latexmk -C -outdir=$(BUILD) $(SOURCE)
	rm -rf $(BUILD) $(TARGET)
