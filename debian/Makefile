prefix = /usr/local

all:
	$(CC) -o ii ii.c

install:
	gcc -o ii ii.c
	echo $(DESTDIR)
	echo $(prefix)
	install ii $(DESTDIR)$(prefix)/bin
	install ii.1 $(DESTDIR)$(prefix)/share/man/man1

clean:
	rm -f ii
