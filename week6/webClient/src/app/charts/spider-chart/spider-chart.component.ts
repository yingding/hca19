import { Component, OnInit } from '@angular/core';

import * as Highcharts from 'highcharts'
import ExportingModule from 'highcharts/modules/exporting'
import MoreModule from 'highcharts/highcharts-more'
// import ExportDataModule from 'highcharts/modules/export-data'
// ExportData has some issue with exporting module

MoreModule(Highcharts); //
ExportingModule(Highcharts);
// ExportDataModule(Highcharts); allow data as csv download


// https://www.highcharts.com/blog/tutorials/highcharts-angular-wrapper/

@Component({
  selector: 'app-spider-chart',
  templateUrl: './spider-chart.component.html',
  styleUrls: ['./spider-chart.component.scss']
})
export class SpiderChartComponent implements OnInit {
  // required by Highcharts-angular wrapper
  // highcharts: typeof Highcharts = Highcharts;
  Highcharts = Highcharts;
  chartConstructor = 'chart';
  chartOptions;

  constructor() { }

  ngOnInit() {
    this.chartOptions =
      {

        chart: {
          polar: true,
          type: 'line'
        },
        credits: {
          enabled: false
        },

        title: {
          text: this.constructor.name + ': '+ 'Budget vs spending',
          x: -80
        },

        pane: {
          size: '80%'
        },

        xAxis: {
          categories: ['Sales', 'Marketing', 'Development', 'Customer Support',
            'Information Technology', 'Administration'],
          tickmarkPlacement: 'on',
          lineWidth: 0
        },

        yAxis: {
          gridLineInterpolation: 'polygon',
          lineWidth: 0,
          min: 0
        },

        tooltip: {
          shared: true,
          pointFormat: '<span style="color:{series.color}">{series.name}: <b>${point.y:,.0f}</b><br/>'
        },

        legend: {
          align: 'right',
          verticalAlign: 'top',
          y: 70,
          layout: 'vertical'
        },

        series: [{
          name: 'Allocated Budget',
          data: [43000, 19000, 60000, 35000, 17000, 10000],
          pointPlacement: 'on'
        }, {
          name: 'Actual Spending',
          data: [50000, 39000, 42000, 31000, 26000, 14000],
          pointPlacement: 'on'
        }]

      }
  }
}
