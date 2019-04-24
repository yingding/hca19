import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { DialogOverviewExampleDialog} from "./dialog.overview.example.dialog";

// material design
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatButtonModule, MatDialogModule, MAT_DIALOG_DEFAULT_OPTIONS} from "@angular/material";

@NgModule({
  declarations: [
    AppComponent,
    DialogOverviewExampleDialog
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatDialogModule
  ],
  //providers: [{provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: false}}],
  entryComponents: [DialogOverviewExampleDialog],
  /**
   * adding dynamically created components to entryComponents:
   * https://stackoverflow.com/questions/41519481/angular2-material-dialog-has-issues-did-you-add-it-to-ngmodule-entrycomponent
   */

  bootstrap: [AppComponent]
})
export class AppModule { }
