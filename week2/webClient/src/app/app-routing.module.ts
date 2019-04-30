import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

// importing the components
import {LoginComponent} from "./login/login.component";
import {WelcomeComponent} from "./welcome/welcome.component";
import {AppComponent} from "./app.component";
import {UserHomeComponent} from "./private/user-home/user-home.component";
// import {UserHomeComponent} from "./private/user-home/user-home.component";


const routes: Routes = [
  {path: '', redirectTo: '/welcome', pathMatch: 'full'}, // Default route
  //This route redirects a URL that fully matches the empty path to the route whose path is '/welcome'.
  {path: 'welcome', component: WelcomeComponent},
  {path: 'login', component: LoginComponent},
  // {path: 'home', component: UserHomeComponent}, // the private content entry component
  // {path: '**', component: AppComponent}, // PageNotFound
  /* while home is not defined in app-routing but in private module routing
   * localhost:port/home lead to PageNotFound
   */
];

// Find more details about RouterModule https://angular.io/guide/router
@NgModule({
  imports: [RouterModule.forRoot(routes)], // use forRoot(routes, {enableTracking: true}) for debugging purposes
  exports: [RouterModule]
})
export class AppRoutingModule { }
