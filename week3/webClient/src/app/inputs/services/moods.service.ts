import { Injectable } from '@angular/core';
import { Http, Response, Headers, RequestOptions} from '@angular/http';
import {Observable} from 'rxjs';
import { map } from 'rxjs/operators';
import {MoodModel} from '../models/mood-model';

// @Injectable({
//   providedIn: 'root'
// })
@Injectable()
export class MoodsService {
  private API_URL_GET: string = "api/moods/get/";
  private API_URL_POST: string = "api/moods/post/";


  constructor(private http: Http) {
  }

  getMoods(): Observable<MoodModel[]> {
    const headers = new Headers({'Content-Type': 'application/json'});
    const httpOptions = new RequestOptions({headers: headers});
    const body = {
      seed:  "seedToChange",
    };
    // the wrapper object from the responsebody has the property name moods, which is an Array
    return this.http.post(this.API_URL_GET, body, httpOptions).pipe(
      map(
      response => response.json().moods as MoodModel[]
      )
    );
  }

  sendMoods(moods: MoodModel[]): Observable<Response> {
    // construct a request header, for json content
    const headers = new Headers({'Content-Type': 'application/json'});
    const httpOptions = new RequestOptions({headers: headers});
    const body = {
      seed:  "seedToChange",
      moods: moods,
    };
    return this.http.post(this.API_URL_POST, body, httpOptions);
  }
}
