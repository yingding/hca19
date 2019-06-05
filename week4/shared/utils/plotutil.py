import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
# register panda converter
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# from pandas.tseries import converter
# converter.register()

class PlotUtil:
    # TODO: need be tested , still buggy
    @classmethod
    def ploting(cls, xvals, yvals, xlabel_str, ylabel_str, title, style, label, grid=True):
        """
        creates a plot of time series data

        """
        # close all old plots
        plt.close("all")

        myFormatter = DateFormatter('%m/%d/%y')
        # myFormatter = DateFormatter("%H:%M")

        # plotting
        fig, ax = plt.subplots()
        fig.set_size_inches(12, 3.5) # you can set it to 15, 3.5 to make the cell width longer
        ax.plot_date(xvals, yvals, fmt=style, label=label)

        # print("xvals", xvals)
        # print("yvals", yvals)
        # ax.plot(xvals, yvals, label = label)

        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)

        ax.xaxis.set_major_formatter(myFormatter)

        plt.xlabel(xlabel_str)
        plt.ylabel(ylabel_str)
        plt.title(title)
        # show the grid line/ help line in plot
        plt.grid(grid)
        #plt.legend(loc='upper right')
        #plt.axis([0, 210, 0, 0.04 ])
        #plt.figure(figsize=[9,6])
        plt.show()