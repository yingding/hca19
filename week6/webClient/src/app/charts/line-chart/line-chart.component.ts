import { Component, OnInit } from '@angular/core';
import * as Highcharts from 'highcharts'
import HC_exporting from 'highcharts/modules/exporting'
HC_exporting(Highcharts);

// declare var require: any;
// let Boost = require('highcharts/modules/boost');
// let noData = require('highcharts/modules/no-data-to-display');
// let More = require('highcharts/highcharts-more');
//
// Boost(Highcharts);
// noData(Highcharts);
// More(Highcharts);
// noData(Highcharts);

@Component({
  selector: 'app-line-chart',
  templateUrl: './line-chart.component.html',
  styleUrls: ['./line-chart.component.scss']
})
export class LineChartComponent implements OnInit {
  // required by Highcharts-angular wrapper
  // highcharts: typeof Highcharts = Highcharts;
  Highcharts = Highcharts;
  chartConstructor = 'chart';
  chartOptions;

  constructor() { }

  ngOnInit() {
    this.chartOptions =  {
      title : { text : this.constructor.name + ': '+ 'simple line chart'},
      credits: {
        enabled: false
      },
      series: [
        {
          data: [29.9, 71.5, 106.4, 129.2, 50, 76, 13],
        },
        {
          data: [50, 76, 13, 29.9, 71.5, 106.4, 129.2, 111],
        }
      ]
    }

    // Highcharts.chart('', this.chartOptions);
  }

}
