import { Component, OnInit } from '@angular/core';
// import {InputsModule} from '../../inputs.module'; circular dependency

@Component({
  selector: 'app-input-root',
  templateUrl: './input-root.component.html',
  styleUrls: ['./input-root.component.scss']
})
export class InputRootComponent implements OnInit {
  private componentName : string;
  private moduleName : string;

  constructor() {
    this.moduleName = "InputsModule";
    this.componentName = InputRootComponent.name;
  }

  ngOnInit() {
  }

}
