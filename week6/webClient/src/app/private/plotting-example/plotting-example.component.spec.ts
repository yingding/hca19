import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PlottingExampleComponent } from './plotting-example.component';

describe('PlottingExampleComponent', () => {
  let component: PlottingExampleComponent;
  let fixture: ComponentFixture<PlottingExampleComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PlottingExampleComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PlottingExampleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
