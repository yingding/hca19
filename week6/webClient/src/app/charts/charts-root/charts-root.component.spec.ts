import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChartsRootComponent } from './charts-root.component';

describe('ChartsRootComponent', () => {
  let component: ChartsRootComponent;
  let fixture: ComponentFixture<ChartsRootComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChartsRootComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChartsRootComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
