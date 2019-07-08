import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HighchartsChartModule} from "highcharts-angular";

import { ChartsRoutingModule } from './charts-routing.module';
import { ChartsRootComponent } from './charts-root/charts-root.component';
import { LineChartComponent } from './line-chart/line-chart.component';
import { SpiderChartComponent } from './spider-chart/spider-chart.component';
import { PieChartComponent } from './pie-chart/pie-chart.component';
import { BarChartComponent } from './bar-chart/bar-chart.component';
import { ScatterPlotComponent } from './scatter-plot/scatter-plot.component';
import { ScatterPlot3dComponent } from './scatter-plot-3d/scatter-plot-3d.component';

@NgModule({
  declarations: [ChartsRootComponent, LineChartComponent, SpiderChartComponent, PieChartComponent, BarChartComponent, ScatterPlotComponent, ScatterPlot3dComponent],
  imports: [
    HighchartsChartModule, // Hightcharts-angular official Wrapper
    CommonModule,
    ChartsRoutingModule
  ],
  exports: [
    ChartsRootComponent
  ]
})
export class ChartsModule { }
