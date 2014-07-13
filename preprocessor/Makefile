all: defer.preproc.c concatenate.preproc.c

defer.preproc.c: defer.c
	gcc -E defer.c > defer.preproc.c

concatenate.preproc.c: concatenate.c
	gcc -E concatenate.c > concatenate.preproc.c

