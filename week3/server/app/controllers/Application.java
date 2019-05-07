package controllers;

import play.Logger;
import play.mvc.Controller;
import play.mvc.Result;

import javax.inject.Inject;
import javax.inject.Singleton;

/**
 */
@Singleton
public class Application extends Controller {

    public Result show(String page) {
        Logger.info(page);
        return redirect("/");
        //return redirect(controllers.routes.Assets.at(path="/public", file="index.html")).as("text/html");
    }
}
