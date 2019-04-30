import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";

@Component({
  selector: 'app-user-home',
  templateUrl: './user-home.component.html',
  styleUrls: ['./user-home.component.scss']
})
export class UserHomeComponent implements OnInit {

  constructor(private router: Router) {}

  ngOnInit() {
  }

  logout(): void {
    this.router.navigate(["/welcome"]);
    // this.router.navigate(["/welcome"], {relativeTo: this.route});
    // the use of relativeTo sees not necessary any more in contrary to what is stated in the reference: https://stackoverflow.com/questions/37196882/how-do-i-navigate-to-a-parent-route-from-a-child-route
  }
}
