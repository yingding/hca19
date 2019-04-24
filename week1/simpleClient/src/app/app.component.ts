import { Component, ViewEncapsulation} from '@angular/core';
import {MatDialog} from "@angular/material";
import {DialogOverviewExampleDialog} from "./dialog.overview.example.dialog";

export interface DialogData {
  text: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
  // encapsulation: ViewEncapsulation.None,
})
// https://stackoverflow.com/questions/34542143/load-external-css-style-into-angular-2-component

export class AppComponent {
  title: string = 'simpleClient';
  success_str : string = "Your setup works fine!";

  constructor(public dialog: MatDialog){}

  // deprecated
  onClick() {
    alert(this.success_str);
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(DialogOverviewExampleDialog, {
      width: '250px',
      data: {text: this.success_str}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      // data.text is given back as result.
      // console.log(result)
    });
  }
}

