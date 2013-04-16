results: 
	python simulate.py

graphs: 
	gnuplot graph1.plt
	gnuplot graph2.plt
	gnuplot graph3.plt
	gnuplot graph4.plt
	
clean:
	rm -fv *.png
	rm -fv *~

reset: clean
	rm -fv *.dat
