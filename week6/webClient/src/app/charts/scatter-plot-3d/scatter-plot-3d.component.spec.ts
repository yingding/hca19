import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ScatterPlot3dComponent } from './scatter-plot-3d.component';

describe('ScatterPlot3DComponent', () => {
  let component: ScatterPlot3dComponent;
  let fixture: ComponentFixture<ScatterPlot3dComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScatterPlot3dComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ScatterPlot3dComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
