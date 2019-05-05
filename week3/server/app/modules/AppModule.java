package modules;

import com.google.inject.AbstractModule;
import play.Environment;
// import play.Configuration;
import com.typesafe.config.Config;
import play.Logger;
import services.AppConfigService;
import services.DaemonService;

/**
 * @Author: Yingding Wang on 07.05.17.
 */
public class AppModule extends AbstractModule {

    private final Environment environment;
    private final Config configuration;
    // private final Configuration configuration;

    public AppModule(Environment environment, Config configuration) {
        this.environment = environment;
        this.configuration = configuration;
    }

    @Override
    public void configure() {
        // final Config sysVars = configuration; // not necessary, since this is no play.Configuration
        // and the config file is already initialized.

        // final Configuration sysVars = configuration.getConfig("myApp");

        //Configuration config = configuration.getConfig("app");
        Logger.info("Starting Demo Server");

        // Ask Guice to create an instance of AppConfigService when the application starts
        bind(AppConfigService.class).asEagerSingleton();
        // Ask Guice to create an instance of AppMongoClientFactory when the application starts
        bind(DaemonService.class).asEagerSingleton();

    }
}
