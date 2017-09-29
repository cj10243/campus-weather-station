
    $(document).ready(function () {
        var endpoint = '/status';
        var temperature = [];
        var humidity = [];
        var uv = [];
        var light = [];
        var rainfall = [];
        var labels = [];
        $.ajax({
            method: "GET"
            , url: endpoint
            , success: function (data) {
                labels = data.labels;
                temperature = data.temperature;
                console.log(temperature);
                setChart(temperature);
            }
            , error: function (error_data) {
                console.log("error");
                console.log(error_data);
            }
        });

        function setChart(temperature) {
            console.log(temperature);
            Highcharts.setOptions({
                title: {
                    text: '過去24小時氣溫變化圖'
                }
                , chart: {
                    backgroundColor: {
                        linearGradient: [0, 0, 500, 500]
                        , stops: [
                               [0, 'rgb(255, 255, 255)']
                               , [1, 'rgb(240, 240, 255)']
                               ]
                    }
                    , borderWidth: 2
                    , plotBackgroundColor: 'rgba(255, 255, 255, .9)'
                    , plotShadow: true
                    , plotBorderWidth: 1
                }
            });
            var chart2 = new Highcharts.Chart({
                chart: {
                    renderTo: 'container2'
                    , type: 'column'
                },
                xAxis: {
                      type: 'datetime',
                      tickInterval: 3600 * 1000,
                      min: Date.UTC(2013,4,22),
                      max: Date.UTC(2013,4,23),
                  }
                    ,series: [{
                    data: temperature
                    //data: [8, 7, 5, 6, 4, 2, 3, 1]
                    , pointStart: Date.UTC(2017, 0, 1)
                    , pointInterval: 3600 * 1000 // one hour
                   }]
            });
            console.log(temperature);
        }

    });