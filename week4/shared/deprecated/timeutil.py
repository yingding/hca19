import datetime

# from pytz import timezone

class TimeUtil:
    # class / static variable epoch, which is associated to class, different from object variable
    # https://stackoverflow.com/questions/68645/static-class-variables-in-python
    epoch = datetime.datetime.utcfromtimestamp(0)
    # print(epoch.tzname())

    @classmethod
    def unix_time_millis(cls, dt):
        """
        this method transforms datetime object to utc timestamp in milliseconds
        :param dt: a utc datetime object
        :return: utc timestamp in milliseconds
        """
        # int() round up the decimals
        return (dt - cls.epoch).total_seconds() * 1000

    @classmethod
    def unix_time_secs(cls, dt):
        """
        this method transforms datetime object to utc timestamp in seconds
        :param dt: a utc datetime object
        :return: utc timestamp in seconds
        """
        return cls.unix_time_millis(dt) / 1000

    @classmethod
    def timestamp_in_secs_2_datetime(cls, timestamp):
        """
        this method transforms the long representation of a utc timestamp to a datetime object
        :param timestamp: long
        :return: datetime object of the timestamp (long) given
        """
        return cls.epoch + datetime.timedelta(seconds=timestamp)

    @classmethod
    def timestamp_in_millisecs_2_datetime(cls, timestamp):
        """
        this method transforms the long representation of a utc timestamp to a datetime object
        :param timestamp: long
        :return: datetime object of the timestamp (long) given
        """
        return cls.epoch + datetime.timedelta(milliseconds=timestamp)

    @classmethod
    def test(cls):
        """
        1494406804593 timestamp in millisecs
        1495574845    23.may.2017 in secs
        :return:
        """
        datetime_now = datetime.datetime.now()
        timestamp_now_in_secs = cls.unix_time_secs(datetime_now)
        timestamp_now_in_millisecs = cls.unix_time_millis(datetime_now)
        print("\n## Testing the timeutil functions")
        print("Datetime Now: {}".format(str(datetime_now)))
        print("Now in utc timestamp in secs:{}".format(timestamp_now_in_secs))
        print("Now in utc timestamp in millisecs:{}".format(timestamp_now_in_millisecs))

    @classmethod
    def str2Datetime(cls, time_string, format='%Y-%m-%d %H:%M', offset=2):
        """
        the format for time string to parse can be found in
        https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        https://www.saltycrane.com/blog/2009/05/converting-time-zones-datetime-objects-python/
        https://www.timeanddate.com/time/zones/cest
        Testing Unix Conventer with
        https://www.epochconverter.com/

        :param time_string:
        :param format:
        :param offset: default is 2 because the EUROPE/BERLIN in summer is 2 hours ahead of UTC time
        :return:
        """
        # get a native gmt time without timezone info
        dt_native_berlin = datetime.datetime.strptime(time_string, format)
        dt = dt_native_berlin - datetime.timedelta(hours=offset)
        # dt_native.replace(tzinfo=Berlin)
        # dt_CEST = timezone('Europe/Berlin').localize(dt_native)
        return dt

    @classmethod
    def datetime2str(cls, dt, format='%Y-%m-%d %H:%M'):
        """
        the format for time string to parse can be found in
        https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        :param dt:
        :param format:
        :return:
        """
        return dt.strftime(format)

class Berlin(datetime.tzinfo):
    def utcoffset(self, *dt):
        return datetime.timedelte(hours=2)

    def tzname(self, dt):
        return "Berlin"

    def dst(self, dt):
        pass