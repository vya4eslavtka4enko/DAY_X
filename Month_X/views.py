from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
from .forms import FileForm
from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
# Global var


def main(request):
    context = {}
    context['form'] = FileForm()
    plot_div='0'
    minimum_price='0'
    average_price=0
    maximum_price = 0
    sorted_data_low = []
    sorted_data_hight = []

    if request.method == "POST":
        path=request.POST
        DATA = pd.read_csv(path['CSV_FILES'], sep=';')
        low_values = [item for item in DATA['low']]
        data_values = [data for data in DATA['timestamp']]
        data_price = find_low_month(low_values,data_values)
        sorted_data = best_month(low_values, data_values)
        sorted_data_low = list(sorted_data)[0][:3]
        sorted_data_hight = list(sorted_data)[1][-3:]
        print(sorted_data_low)
        print(sorted_data_hight)
        average_price = "{:.2f}".format(data_price[2])
        minimum_price =data_price[0]
        maximum_price = data_price[2]
        x_data = data_values
        y_data = low_values
        plot_div = plot([Scatter(x=x_data, y=y_data,
                                        mode='lines', name='test',
                                        opacity=0.8, marker_color='green')],
                                        output_type='div')

    return render(request,'main.html',{'context':context,
                                                            'DATA':plot_div,
                                                            'min_price':minimum_price,
                                                            'average_price':average_price,
                                                            'maximum_price':maximum_price,
                                                            'sorted_data_low':sorted_data_low,
                                                            'sorted_data_hight':sorted_data_hight})


def find_low_month(low_values,data_values):
    minimum_price = 0
    maximum_price = 0
    data = ''
    avarage_price = Average(low_values)
    for index,item in enumerate(low_values,start=1):
        if minimum_price < item:
            minimum_price=item
            data = data_values[low_values.index(item)]
        else:
            continue

    for index,item in enumerate(low_values,start=1):
        if maximum_price > item:
            maximum_price=item
            data = data_values[low_values.index(item)]
        else:
            continue
    return minimum_price,data,avarage_price,maximum_price

def Average(lst):
    return sum(lst)/len(lst)

def best_month(low_values,data_values):
    combined_lists = list(zip(low_values, data_values))
    sorted_combined = sorted(combined_lists, key=lambda x: x[0])
    return sorted_combined[:3],sorted_combined[-3:]

def get_current_price():
    pass





