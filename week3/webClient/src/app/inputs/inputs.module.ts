import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { InputsRoutingModule } from './inputs-routing.module';
import { InputRootComponent } from './input-root/input-root.component';
import { InputMoodComponent } from './input-mood/input-mood.component';

// material input
import { FormsModule} from '@angular/forms'; // FormsModule is needed for the two binding for the Form in AngularMaterial
// material design
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule, MatFormFieldModule, MatInputModule } from '@angular/material';

// import { MoodModel } from './models/mood-model'; // why shouldn't moodModel be declared in the Module?
// import {HttpClientModule} from '@angular/common/http';

import {HttpModule} from '@angular/http';

@NgModule({
  declarations: [InputRootComponent, InputMoodComponent],
  imports: [
    CommonModule,
    InputsRoutingModule,
    FormsModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatFormFieldModule,
    MatInputModule,
    // HttpClientModule,
    HttpModule
  ],
  exports: [
     InputRootComponent
  ]
})
export class InputsModule { }
