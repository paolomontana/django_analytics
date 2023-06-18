from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from apps.home import core


@csrf_exempt
def getDatasetTable(request):
    if request.method == 'POST':
        urlDataSet = request.POST['dataset_url']
        if 'number_row' in request.POST:
            dataset = core.readDataset(
                urlDataSet, int(request.POST['number_row']))
        else:
            dataset = core.readDataset(urlDataSet)

        tableHtml = core.buildTable(dataset)
        selectColumnsHtml = core.buildSelect(dataset)
        json={'tableHtml':tableHtml, 'selectColumnsHtml':selectColumnsHtml}

    return JsonResponse(json)
  

@csrf_exempt
def plotDataset(request):
    if request.method == 'POST':
        urlDataSet = request.POST['dataset_url']
        xPlot = request.POST['x_plot']
        yPlot = request.POST['y_plot']
        dataset = core.readDataset(urlDataSet)
        imgHtml = core.buildImgGraph(dataset,xPlot,yPlot)
    return HttpResponse(imgHtml)
