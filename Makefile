dataset: 
	python simulate.py

graphs: 
	gnuplot plots/plot_cvd_lin.plt
	gnuplot plots/plot_cvd_log.plt
	gnuplot plots/plot_dvd.plt
	gnuplot plots/plot_fvd.plt
	gnuplot plots/plot_pvd.plt

clean:
	rm -fv *.png
	rm -fv *~
	rm -fv *.dat
