import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HighchartsChartModule} from "highcharts-angular";

import { ChartsRoutingModule } from './charts-routing.module';
import { ChartsRootComponent } from './charts-root/charts-root.component';
import { LineChartComponent } from './line-chart/line-chart.component';

@NgModule({
  declarations: [ChartsRootComponent, LineChartComponent],
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
