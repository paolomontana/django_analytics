import pandas as pd
import json
import urllib
import matplotlib.pyplot as plt
import matplotlib
import time

import os
from django.conf import settings


def readDataset(url, numberRow=0):

    data = json.load(urllib.request.urlopen(url))
    dfItem = pd.DataFrame.from_records(data)
    if (numberRow > 0):
        dfItem = dfItem.head(numberRow)
    return dfItem


def buildTable(dataSet):
    tableHtml = '<thead class="thead-light">'
    tableHtml += '<tr>'
    for name in dataSet.columns:
        tableHtml += '<th scope="col">'+name+'</th>'
    tableHtml += '</tr>'
    tableHtml += '</thead>'
    tableHtml += '<tbody>'

    for index, row in dataSet.iterrows():
        tableHtml += '<tr>'

        for name in dataSet.columns:
            tableHtml += '<td> '
            tableHtml += str(row[name])
            tableHtml += '</td>'
        tableHtml += '</tr>'

    tableHtml += '</tbody>'
   # print(tableHtml)
    return tableHtml


def buildSelect(dataSet):
    html = ""
    for name in dataSet.columns:
        html += '<option value="'+name+'">'+name+'</option>'
    return html


def buildImgGraph(dataSet, xPlot, yPlot):

    x = dataSet[xPlot]
    y = dataSet[yPlot]

    matplotlib.use('SVG')
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()
    plt.plot(x, y)
    plt.xlabel(xPlot)
    plt.ylabel(yPlot)

    fileName = str(round(time.time() * 1000))+"graph.png"
    plt.savefig(os.path.join(settings.BASE_DIR,
                'apps/static/img/'+fileName), format="png")

    return "img/"+fileName
