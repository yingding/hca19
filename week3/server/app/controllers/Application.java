package controllers;

import play.mvc.Controller;
import play.mvc.Result;

import javax.inject.Inject;
import javax.inject.Singleton;

/**
 */
@Singleton
public class Application extends Controller {

    public Result show(String url) {
        return redirect(url);
        //return redirect(controllers.routes.Assets.at(path="/public", file="index.html")).as("text/html");
    }
}
