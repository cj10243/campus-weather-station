from django.shortcuts import render
from weather.models import Weather
from bokeh.models.widgets import Dropdown
from bokeh.plotting import figure
from bokeh.embed import components
def status(request):
    plot = figure()

    plot.circle([1,2], [3,4],[1,2], [3,4],[1,2], [3,4],[1,2], [3,4])

    script, div = components(plot)


    return render(request, 'pages/status.html', {'div': div,'script':script})

'''
def draw(number,title):
    #weather = Weather.objects.all()
    plot = figure(logo=None,x_axis_type="datetime",title="{}".format(title),plot_height=500,plot_width=500)
    plot.line([i for i in range(0,100)],[i for i in range(0,100)])
    template = get_template('status.html')

    script, div = components(grid, button_group)
    html = template.render(locals())
    return HttpResponse(html)
# Create your views here.
'''