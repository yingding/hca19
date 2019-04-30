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

# A quick Angular Tutorial
Go to [Angular Tutorial](AngularTutorial.md)

# References
* Reference Page of Angular is <a href="https://angular.io/docs" target="_blank">https://angular.io/docs</a>
* Introduction of [Configuring browser compatibility]( 
https://angular.io/guide/build#configuring-browser-compatibility)
* Introduction of [Webpack Dev Server Proxy](https://webpack.js.org/configuration/dev-server/#devserver-proxy)
* Introduction of [Webpack Dev Server Configuration](https://webpack.js.org/configuration/dev-server/#devserver-proxy)

* Webpack Configuration Parameters on Github <a href="https://github.com/webpack/docs/wiki/configuration" target="_blank">https://github.com/webpack/docs/wiki/configuration</a>
