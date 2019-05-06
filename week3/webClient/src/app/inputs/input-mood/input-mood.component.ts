import { Component, OnInit } from '@angular/core';
import {MoodModel} from '../models/mood-model';
import * as moment from 'moment';
import {MoodsService} from '../services/moods.service';
import {SharedRefreshService} from '../services/shared-refresh.service';
import {Response} from '@angular/http';

@Component({
  selector: 'app-input-mood',
  templateUrl: './input-mood.component.html',
  styleUrls: ['./input-mood.component.scss']
})
export class InputMoodComponent implements OnInit {

  private moods: MoodModel[] = [];
  private responseMessage: string = null;
  private responseMessageColor: string = null;
  private refresh: boolean = false;
  private mood: string = "";

  constructor(private moodService: MoodsService, private sharedRefreshService: SharedRefreshService) {
  }

  ngOnInit() {
  }

  cacheData(inputElement: HTMLInputElement) {
    // moment format can be found https://momentjs.com/docs/#/displaying/
    const now = moment().format('dddd, MMMM Do YYYY, h:mm:ss a');
    const nowTimeStamp = moment().utc().valueOf();
    const currentMood = new MoodModel(nowTimeStamp, this.mood.toUpperCase());
    console.log("currentDateString: ", now);
    console.log("currentUTCtimestamp: ", currentMood.timestamp);
    console.log("call service: ", currentMood.mood);
    this.moods.push(currentMood);
    inputElement.value = null; // clean the value
  }

  sendData() {
    this.moodService.sendMoods(this.moods).subscribe(
      response => this.handleResponse(response),
      error => this.handleResponse(error)
    );
    // refresh is true
    this.refresh = !this.refresh; // switch
    this.sharedRefreshService.publishData(this.refresh);
  }

  handleResponse(response: Response) {
    if (response.ok) {
      this.responseMessage = response.text();
      this.responseMessageColor = 'lawngreen';
      this.moods = []; // clear the moods
    } else {
      this.responseMessage = response.text();
      this.responseMessageColor = 'red';
    }
  }

}
