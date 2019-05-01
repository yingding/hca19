import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// material design
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule, MatDialogModule, MatFormFieldModule, MatInputModule} from '@angular/material';
// adding components to this module
import { LoginComponent } from './login/login.component';
import { WelcomeComponent } from './welcome/welcome.component';
import { PopupDialogComponent } from './shared/dialog/popup-dialog/popup-dialog.component';
import { PrivateModule } from './private/private.module';
import { PageNotFoundComponent } from './shared/component/page-not-found/page-not-found.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    WelcomeComponent,
    PopupDialogComponent,
    PageNotFoundComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatDialogModule,
    MatFormFieldModule,
    MatInputModule,
    PrivateModule,
    AppRoutingModule, // the subModule with Module routes must be placed above the AppRoutingModule
  ],
  // providers: [{provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: false}}],
  entryComponents: [PopupDialogComponent],
  /**
   * adding dynamically created components to entryComponents:
   * https://stackoverflow.com/questions/41519481/angular2-material-dialog-has-issues-did-you-add-it-to-ngmodule-entrycomponent
   */

  bootstrap: [AppComponent]
})
export class AppModule { }
