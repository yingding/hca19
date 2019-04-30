import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PrivateRoutingModule } from './private-routing.module';
import { DashBoardComponent } from './dash-board/dash-board.component';
import { AboutComponent } from './about/about.component';
import { UserHomeComponent } from './user-home/user-home.component';
import { MatButtonModule } from "@angular/material";


@NgModule({
  declarations: [DashBoardComponent, AboutComponent, UserHomeComponent],
  imports: [
    CommonModule,
    PrivateRoutingModule,
    MatButtonModule
  ]
})
export class PrivateModule { }
