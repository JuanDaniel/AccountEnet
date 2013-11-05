# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 31/10/2013

@author: jdsantana
'''


import os
import json

class Graphic():
    '''
    It class obtain the data access and prepare to paint
    '''

    def __init__(self, acces):
        self.__access = acces

    def generatePie(self):
        phones = {}
        total_time = '0:0:0'
        for a in self.__access:
            if(not phones.has_key(a['phone'])):
                phones[a['phone']] = {'consume':'0:0:0', 'percent':0}

            phones[a['phone']]['consume'] = self.__sumConsume(a['duration'], phones[a['phone']]['consume'])

            total_time = self.__sumConsume(total_time, a['duration'])

        total_time = '%s:%s:%s' %(self.__convertTime(total_time))
        total = self.__convertToNum(total_time)

        series = ""
        for phone in phones:
            phones[phone]['consume'] = '%s:%s:%s' %(self.__convertTime(phones[phone]['consume']))
            phones[phone]['percent'] = round(float(self.__convertToNum(phones[phone]['consume']) * 100) / total, 2)
            series = series + "['" + phone + "', " + str(phones[phone]['percent']) + "],"

        html = """
                <!DOCTYPE HTML>
                <html>
                    <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                        <title>Consumo por teléfono</title>

                        <script type="text/javascript" src="../js/jquery-1.9.1.js"></script>
                        <script type="text/javascript">
                            $(function () {
                                    $('#container').highcharts({
                                        chart: {
                                            plotBackgroundColor: null,
                                            plotBorderWidth: null,
                                            plotShadow: false
                                        },
                                        title: {
                                            text: 'Consumo de la cuenta para cada teléfono'
                                        },
                                        tooltip: {
                                            formatter: function(){
                                                return 'El teléfono <b> '+ this.point.name +'</b> ha consumido un '+ Highcharts.numberFormat(this.percentage, 2) +'%';
                                            }
                                        },
                                        plotOptions: {
                                            pie: {
                                                allowPointSelect: true,
                                                cursor: 'pointer',
                                                dataLabels: {
                                                    enabled: true,
                                                    color: '#000000',
                                                    connectorColor: '#000000',
                                                    formatter: function() {
                                                        return '<b>'+ this.point.name +'</b>: '+ Highcharts.numberFormat(this.percentage, 2) +' %';
                                                    }
                                                }
                                            }
                                        },
                                        series: [{
                                            type: 'pie',
                                            name: 'Comsumo',
                                            data: [""" + series + """]
                                        }]
                                    });
                                });
                        </script>
                    </head>
                    <body>
                        <script src="../js/highcharts.js"></script>
                        <div id="container" style="min-width: 600px; min-height: 450px; margin: 0 auto"></div>
                    </body>
                </html>"""

        file = open(os.path.join('Extras', 'highcharts', 'pie-basic', 'index.html'), 'w')
        file.writelines(html)
        file.close()

    def generatePolygon(self):
        phones = {}
        for a in self.__access:
            if(not phones.has_key(a['phone'])):
                phones[a['phone']] = {'days':{}}

            days = phones[a['phone']]['days']

            if(not days.has_key(a['date_start'])):
                days[a['date_start']] = '0:0:0'

            days[a['date_start']] = self.__sumConsume(days[a['date_start']], a['duration'])

        series = []
        for phone in phones:
            pd = {}
            pd['name'] = phone
            pd['data'] = []
            for i in range(1, 32):
                exist = False
                for date_start in phones[phone]['days']:
                    day = date_start.split('-')[2]
                    if(i == int(day)):
                        consume = self.__convertToNum(phones[phone]['days'][date_start])
                        pd['data'].append(consume)
                        exist = True
                        del phones[phone]['days'][date_start]
                        break
                if(not exist):
                    pd['data'].append(0)

            series.append(pd)

        html = """
                <!DOCTYPE HTML>
                <html>
                    <head>
                        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                        <title>Consumo por teléfono</title>

                        <script type="text/javascript" src="../js/jquery-1.9.1.js"></script>
                        <script type="text/javascript">
                            $(function () {
                                $('#container').highcharts({
                                    chart: {
                                        type: 'line',
                                        marginRight: 130,
                                        marginBottom: 25
                                    },
                                    title: {
                                        text: 'Consumo diario por cada teléfono',
                                        x: -20 //center
                                    },
                                    xAxis: {
                                        categories: ['1', '2', '3', '4', '5', '6',
                                            '7', '8', '9', '10', '11', '12', '13', '14', '15',
                                            '16', '17', '18', '19', '20', '21', '22', '23', '24',
                                            '25', '26', '27', '28', '29', '30', '31']
                                    },
                                    yAxis: {
                                        title: {
                                            text: 'Consumo (minutos)'
                                        },
                                        plotLines: [{
                                            value: 0,
                                            width: 1,
                                            color: '#808080'
                                        }]
                                    },
                                    tooltip: {
                                        formatter: function(){
                                                return 'Día ' + this.x +'<br />El teléfono <b> '+ this.series.name +'</b> ha consumido '+ this.y +' minutos';
                                            }
                                    },
                                    legend: {
                                        layout: 'vertical',
                                        align: 'right',
                                        verticalAlign: 'top',
                                        x: -10,
                                        y: 100,
                                        borderWidth: 0
                                    },
                                    series: """ + json.dumps(series) + """
                                });
                            });
                        </script>
                    </head>
                    <body>
                        <script src="../js/highcharts.js"></script>
                        <div id="container" style="min-width: 600px; min-height: 450px; margin: 0 auto"></div>
                    </body>
                </html>"""

        file = open(os.path.join('Extras', 'highcharts', 'line-basic', 'index.html'), 'w')
        file.writelines(html)
        file.close()

    def __sumConsume(self, d1, d2):
        new_hour, new_min, new_seg = d1.split(':')
        old_hour, old_min, old_seg = d2.split(':')

        hour = int(new_hour) + int(old_hour)
        min = int(new_min) + int(old_min)
        seg = int(new_seg) + int(old_seg)

        consume = "%s:%s:%s" % (hour, min, seg)

        return consume

    def __convertTime(self, time):
        '''
        Created by ybarrio
        '''
        hour, min, seg = time.split(":")

        rest, seg = divmod(int(seg), 60)

        min = int(min) + rest
        rest, min = divmod(min, 60)

        hour = int(hour) + rest

        '''
        Convert the values to format 00:00:00
        '''
        if(hour < 10):
            hour = '0%s'%(hour)
        if(min < 10):
            min = '0%s'%(min)
        if(seg < 10):
            seg = '0%s'%(seg)

        return hour, min, seg

    def __convertToNum(self, consume):
        '''
        Convert the consume to minutes
        '''
        hour, min, seg = consume.split(":")

        return int(hour) * 60 + int(min) + int(seg) / 60