dataset: 
	mkdir -p datasets/
	python simulate.py

graphs: 
	mkdir plots/images/
	gnuplot plots/plot_cvd_lin.plt
	gnuplot plots/plot_cvd_log.plt
	gnuplot plots/plot_dvd.plt
	gnuplot plots/plot_fvd.plt
	gnuplot plots/plot_pvd.plt

clean:
	rm -rfv plots/images/
	rm -rfv datasets/
