import { TestBed } from '@angular/core/testing';

import { MoodsServiceService } from './moods-service.service';

describe('MoodsServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: MoodsServiceService = TestBed.get(MoodsServiceService);
    expect(service).toBeTruthy();
  });
});
