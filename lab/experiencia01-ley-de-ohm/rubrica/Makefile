ENGINE ?= lualatex
SOURCE = rubrica-reporte01.tex
TARGET = rubrica-reporte01.pdf
BUILD = build

.PHONY: pdf clean

pdf:
	mkdir -p $(BUILD)
	latexmk -$(ENGINE) -interaction=nonstopmode -halt-on-error -outdir=$(BUILD) $(SOURCE)
	cp $(BUILD)/$(TARGET) $(TARGET)

clean:
	latexmk -C -outdir=$(BUILD) $(SOURCE)
	rm -rf $(BUILD) $(TARGET)
