FPC = fpc
SOURCES = cradle.pas
EXECUTABLES = cradle

default: $(SOURCES)
	$(FPC) $(SOURCES)
	@rm *.o

.PHONY: clean
clean:
	@-rm *.o
	@for exe in $(EXECUTABLES) ; do \
		rm $$exe ; \
	done
