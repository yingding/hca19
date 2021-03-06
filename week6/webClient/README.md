# 0 Learning goal of this tutorial
* Get familiar with different charts

## 0.1 (Optional) Installing the libs
* `npm install highcharts --save`
* `npm install highcharts-angular --save`

Notice: highcharts-more and highcharts-3d can be directly imported from `highcharts/highcharts-more` and `highcharts/highcharts-3d`, no additional npm package needs to be installed.

## 0.2 HighCharts Demo
* https://www.highcharts.com/demo
* https://www.highcharts.com/demo/pie-basic

Note: While examining the highcharts demo, open the view options, than copy the options for the chart you are interested.

## 0.3 HighCharts Angular7+ Wrapper Examples
* [highcharts-angular Wrapper Doc](https://github.com/highcharts/highcharts-angular/blob/master/README.md)
* [highcharts-angular Blog post: using official wrapper](https://www.highcharts.com/blog/tutorials/highcharts-angular-wrapper/)
* [highcharts-angular Blog post: fetching data](https://www.highcharts.com/blog/post/highcharts-and-angular-7/)


## 0.4 HighChart Offline Export
* https://www.highcharts.com/docs/export-module/client-side-export

## 0.5 Todo:
load your data to the plots



# 1. Introduction of this Angular7 seed in Linux and Macosx
* change to the simpleClient directory with `cd webClient`
* Install the local node_modules directory with `npm install`
* Run ng application in dev mode with `npm start`
* Build your code for production with `npm run build`
* Deploy client code to the local server with `npm run deploy`
   <!-- remove the previous dist with `rimraf dist`-->
* Run karma unit test with `npm test`

## 1.1 Proxy Settings
Use proxy settings to access local or remote service with Webpack Dev Server
* Use `npm run local-proxy` to use the src/config/local.proxy.json setting to access the local proxy for all `^/api/`calls 

## 1.2 About this project

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 7.3.8.

# 2. Introduction of Angular-cli
change to the workspace folder with `cd webClient`:
* Use `ng help` to see the angular-cli command
* `ng generate component welcome` generates in src/app the welcome folder with welcome.component.xx files.
* `ng generate component shared/dialog/PopupDialog` generates in src/app/shared/dialog/popup-dialog/ folder popup-dialog.component.xx files, for the class name Popup in CamelCase shall be used.
* `ng generate interface shared/interface/DialogData` generates in src/app/shared/interface folder dialog-data.ts file
* `ng generate component login --module=shared.module` to add and generate templates for the additional module: shared. By default `--module=app.module` is applied if none is given, since the app module is the commonly the single module available. For more details please see https://stackoverflow.com/questions/48102863/ng-generate-component-in-subdirectory 

Create a submodule:

* use `ng generate module private/private --module app --flat --routing` to generate the private-routing.module.ts and private.module.ts in src/app/private folder
* use `ng generate component private/DashBoard --module private
` to generate a component for the module private in the folder private src/app/private/
* use `ng generate component private/about --module private` to generate another component for the module private

Create a chart submodule:

* In folder `webClient` run `ng generate module charts/charts --module app --flat --routing` to generate a charts-routing.module.ts and charts.module.ts in src/app/charts
* In folder `webClient` run `ng generate component charts/SpiderChart --module charts` to generate a SpiderChartComponent for charts module in folder `src/app/charts/spider-chart/`

Software Libraries:
* Highcharts: https://www.highcharts.com/demo
* Highcharts-more (highcharts module)
* Highcharts-3d (highcharts module)
* Highcharts-angular: https://github.com/highcharts/highcharts-angular 

## 2.1 Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## 2.2 Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## 2.3 Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `--prod` flag for a production build.

## 2.4 Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## 2.5 Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## 2.6 Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

# Plotting with HighCharts Lib
* using the official HighChart Angular7 Wrapper by installing the HighCharts lib `npm install highcharts-angular highcharts --save`
* Guild of HighCharts-angular https://github.com/highcharts/highcharts-angular

## Example sources
* https://www.highcharts.com/blog/post/highcharts-and-angular-7/
* https://www.highcharts.com/blog/tutorials/highcharts-angular-wrapper/
* https://www.highcharts.com/demo
<!-- using a service to schedule highcharts 
* https://hashnode.com/post/using-highcharts-with-angular-7-cjtpslapj005acfs1cvgo23rp
-->

# A quick Angular Tutorial
Go to [Angular Tutorial](AngularTutorial.md)

# References
* Reference Page of Angular is <a href="https://angular.io/docs" target="_blank">https://angular.io/docs</a>
* Introduction of [Configuring browser compatibility]( 
https://angular.io/guide/build#configuring-browser-compatibility)
* Introduction of [Webpack Dev Server Proxy](https://webpack.js.org/configuration/dev-server/#devserver-proxy)
* Introduction of [Webpack Dev Server Configuration](https://webpack.js.org/configuration/dev-server/#devserver-proxy)

* Webpack Configuration Parameters on Github <a href="https://github.com/webpack/docs/wiki/configuration" target="_blank">https://github.com/webpack/docs/wiki/configuration</a>

# Project Seed Structure

The following is a snapshot of the current project structure.
```
src
├── app
│   ├── app.component.html
│   ├── app.component.scss
│   ├── app.component.spec.ts
│   ├── app.component.ts
│   ├── app.module.ts
│   ├── app-routing.module.ts
│   ├── charts
│   │   ├── bar-chart
│   │   │   ├── bar-chart.component.html
│   │   │   ├── bar-chart.component.scss
│   │   │   ├── bar-chart.component.spec.ts
│   │   │   └── bar-chart.component.ts
│   │   ├── charts.module.ts
│   │   ├── charts-root
│   │   │   ├── charts-root.component.html
│   │   │   ├── charts-root.component.scss
│   │   │   ├── charts-root.component.spec.ts
│   │   │   └── charts-root.component.ts
│   │   ├── charts-routing.module.ts
│   │   ├── line-chart
│   │   │   ├── line-chart.component.html
│   │   │   ├── line-chart.component.scss
│   │   │   ├── line-chart.component.spec.ts
│   │   │   └── line-chart.component.ts
│   │   ├── pie-chart
│   │   │   ├── pie-chart.component.html
│   │   │   ├── pie-chart.component.scss
│   │   │   ├── pie-chart.component.spec.ts
│   │   │   └── pie-chart.component.ts
│   │   ├── scatter-plot
│   │   │   ├── scatter-plot.component.html
│   │   │   ├── scatter-plot.component.scss
│   │   │   ├── scatter-plot.component.spec.ts
│   │   │   └── scatter-plot.component.ts
│   │   ├── scatter-plot-3d
│   │   │   ├── scatter-plot-3d.component.html
│   │   │   ├── scatter-plot-3d.component.scss
│   │   │   ├── scatter-plot-3d.component.spec.ts
│   │   │   └── scatter-plot-3d.component.ts
│   │   └── spider-chart
│   │       ├── spider-chart.component.html
│   │       ├── spider-chart.component.scss
│   │       ├── spider-chart.component.spec.ts
│   │       └── spider-chart.component.ts
│   ├── inputs
│   │   ├── fetch-moods
│   │   │   ├── fetch-moods.component.html
│   │   │   ├── fetch-moods.component.scss
│   │   │   ├── fetch-moods.component.spec.ts
│   │   │   └── fetch-moods.component.ts
│   │   ├── input-mood
│   │   │   ├── input-mood.component.html
│   │   │   ├── input-mood.component.scss
│   │   │   ├── input-mood.component.spec.ts
│   │   │   └── input-mood.component.ts
│   │   ├── input-root
│   │   │   ├── input-root.component.html
│   │   │   ├── input-root.component.scss
│   │   │   ├── input-root.component.spec.ts
│   │   │   └── input-root.component.ts
│   │   ├── inputs.module.ts
│   │   ├── inputs-routing.module.ts
│   │   ├── models
│   │   │   ├── mood-model.spec.ts
│   │   │   └── mood-model.ts
│   │   └── services
│   │       ├── moods.service.spec.ts
│   │       ├── moods.service.ts
│   │       ├── shared-refresh.service.spec.ts
│   │       └── shared-refresh.service.ts
│   ├── login
│   │   ├── login.component.html
│   │   ├── login.component.scss
│   │   ├── login.component.spec.ts
│   │   └── login.component.ts
│   ├── private
│   │   ├── about
│   │   │   ├── about.component.html
│   │   │   ├── about.component.scss
│   │   │   ├── about.component.spec.ts
│   │   │   └── about.component.ts
│   │   ├── binding-examples
│   │   │   ├── binding-child
│   │   │   │   ├── binding-child.component.html
│   │   │   │   ├── binding-child.component.scss
│   │   │   │   ├── binding-child.component.spec.ts
│   │   │   │   └── binding-child.component.ts
│   │   │   ├── binding-examples.component.html
│   │   │   ├── binding-examples.component.scss
│   │   │   ├── binding-examples.component.spec.ts
│   │   │   ├── binding-examples.component.ts
│   │   │   └── binding-parent
│   │   │       ├── binding-parent.component.html
│   │   │       ├── binding-parent.component.scss
│   │   │       ├── binding-parent.component.spec.ts
│   │   │       └── binding-parent.component.ts
│   │   ├── dash-board
│   │   │   ├── dash-board.component.html
│   │   │   ├── dash-board.component.scss
│   │   │   ├── dash-board.component.spec.ts
│   │   │   └── dash-board.component.ts
│   │   ├── plotting-example
│   │   │   ├── plotting-example.component.html
│   │   │   ├── plotting-example.component.scss
│   │   │   ├── plotting-example.component.spec.ts
│   │   │   └── plotting-example.component.ts
│   │   ├── private.module.ts
│   │   ├── private-routing.module.ts
│   │   └── user-home
│   │       ├── user-home.component.html
│   │       ├── user-home.component.scss
│   │       ├── user-home.component.spec.ts
│   │       └── user-home.component.ts
│   ├── shared
│   │   ├── component
│   │   │   └── page-not-found
│   │   │       ├── page-not-found.component.html
│   │   │       ├── page-not-found.component.scss
│   │   │       ├── page-not-found.component.spec.ts
│   │   │       └── page-not-found.component.ts
│   │   ├── dialog
│   │   │   └── popup-dialog
│   │   │       ├── popup-dialog.component.html
│   │   │       ├── popup-dialog.component.scss
│   │   │       ├── popup-dialog.component.spec.ts
│   │   │       └── popup-dialog.component.ts
│   │   └── interface
│   │       └── dialog-data.ts
│   └── welcome
│       ├── welcome.component.html
│       ├── welcome.component.scss
│       ├── welcome.component.spec.ts
│       └── welcome.component.ts
├── assets
├── browserslist
├── config
│   ├── helpers.js
│   └── local.proxy.json
├── environments
│   ├── environment.prod.ts
│   └── environment.ts
├── favicon.ico
├── index.html
├── karma.conf.js
├── main.ts
├── polyfills.ts
├── styles.scss
├── test.ts
├── tsconfig.app.json
├── tsconfig.spec.json
└── tslint.json
```

# Angular Module settings in Intellij
1. `npm install -g @angular/cli` install angular cli globally
2. week3 -> add new module -> static web -> angular cli, add webClient as angular module
3. See more reference about angular cli project in intellij https://www.jetbrains.com/help/idea/angular.html

# References:
* [Angular Providers](https://angular.io/guide/providers)

