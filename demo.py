from phyplot import plot
x=[4,8,12,16,20]
y=[1.2,1.35,1.45,1.56,1.89]
fig=plot.MyPlot({'x/mm':x,'U/V':y},x_label='x/mm')
fig.plot()

