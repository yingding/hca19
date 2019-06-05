import datetime
import calendar
import pytz
from collections import namedtuple

class TimeUtil():
    """
    this TimeUtil class only implements classmethods, so that these classmethods can be inherit by the subclasses
    """

    # def __init__(self):
    #     self.epoch = datetime.datetime.utcfromtimestamp(0)
    #
    # ## dt must be a utc time
    # def unix_time_millis(self, dt):
    #     return (dt - self.epoch).total_seconds() * 1000.0
    #
    # def unix_time_secs(self, dt):
    #     return (dt - self.epoch).total_seconds() * 1.0

    @classmethod
    def segment_begin_by_timestamp(cls, timestamp_in_sec: int, timeshift: int = 0) -> int:
        """
        Get the begin timestamp of a segment which contains the given timestamp in secs, the segment length is 600 secs.

        :param timestamp_in_sec: timestamp belongs to a segment in secs
        :param timeshift: the timeshift to the beginning of the day in secs
        :return: the begin timestamp of a segment which contains the given timestamp
        """
        return cls.get_segment_by_timestamp(timestamp_in_sec, timeshift = timeshift, interval_in_sec= 600).begin

    # Docstring in Python3
    # https://www.datacamp.com/community/tutorials/docstrings-python
    # https://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
    @classmethod
    def get_segment_by_timestamp(cls, timestamp_in_sec: int, timeshift: int = 0, interval_in_sec: int = 600) -> int:
        """
        Get the segment of the given timestamp

        :param timestamp_in_sec: timestamp belongs to the returning segment
        :param timeshift: the timeshift to the beginning of the day
        :param interval_in_sec: length of the segment in sec, 600 secs is the default value
        :return: the begin and end of the segment containing the given timestamp

        :Example:

        Example 1

        >>> timestamp = 1557481029 # 2019-05-10 11:37:09
        >>> segment = begin_timestamp_of_segment(timestamp)
        >>> segment.begin
        >>> segment.end

        this returns
        \n segment.begin = 1557480600, which is the time 2019-05-10 11:30:00
        \n segment.end = 1557481200, which is the time 2019-05-10 11:40:00

        Example 2: timeshift with 300 secs

        >>> segment = begin_timestamp_of_segment(timestamp, timeshift = 300)
        >>> segment.begin
        >>> segment.end

        this returns
        \n# segment.begin = 1557480900, which is the time 2019-05-10 11:35:00
        \n# segment.end   = 1557481500, which is the time 2019-05-10 11:45:00

        Example 3: timeshift with 120 secs and interval 300 secs

        >>> segment = begin_timestamp_of_segment(timestamp, timeshift = 120, interval = 300)
        >>> segment.begin
        >>> segment.end

        this returns
        \n# segment.begin = 1557481020, which is the time 2019-05-10 11:37:00
        \n# segment.end   = 1557481320, which is the time 2019-05-10 11:42:00
        """
        begin = timestamp_in_sec - (timestamp_in_sec % interval_in_sec) + timeshift
        end = begin + interval_in_sec
        return namedtuple('segment', ['begin', 'end'])(begin, end)

    @classmethod
    def utcTimestamp2dtWithTz(cls, timestampInSec: int, tzinfo: str) -> datetime.datetime:
        """
        https://stackoverflow.com/questions/25264811/pytz-converting-utc-and-timezone-to-local-time
        """
        tz = pytz.timezone(tzinfo)
        # convert the timestamp to a timezone not aware datetime object
        utc_time = datetime.datetime.utcfromtimestamp(timestampInSec)
        # shift the time by setting the timezone
        local_datetime = pytz.utc.localize(utc_time, is_dst=None).astimezone(tz)
        # utc_time.replace(tzinfo=pytz.utc).astimezone(tz) # this one just replay the tz do not add the time shift.
        return local_datetime

    @classmethod
    def utcTimestamp2dt(cls, timestampInSec: int) -> datetime.datetime:
        """
        this method returns a datetime object with timezone Europe/Berlin

        :param timestampInSec: utc timestamp in secs as int, NOT millisecs from the db.
        :return: datetime object with tzinfo = "Europe/Berlin"

        :Example:

        >>> now = dt.datetime.now()
        >>> print(now.tzinfo) # display None
        >>> print(now)

        this returns 2019-05-08 19:00:30.082342

        While:

        >>> mydt = dt.datetime.utcfromtimestamp(timestamp);
        >>> print(mydt)

        returns 2019-05-08 17:00:30

        By calling this method, the time shift for the timezone "Europe/Berlin" is added automatically.

        >>> print(TimeUtil.utcTimestamp2dt(timestamp))

        returns 2019-05-08 19:00:30+02:00
        """
        return cls.utcTimestamp2dtWithTz(timestampInSec, "Europe/Berlin")

    @classmethod
    def dt2dtWithTz(cls, dt: datetime.datetime, tzinfo: str) -> datetime.datetime:
        mytz = pytz.timezone(tzinfo);
        return mytz.normalize(mytz.localize(dt, is_dst=True))

    @classmethod
    def dt2UTCtimestampWithTz(cls, dt: datetime.datetime, tzinfo: str) -> int:
        """
        tzinfo = "Europe/Berlin", or other timezone str from http://pytz.sourceforge.net/
        """
        dt_tz = cls.dt2dtWithTz(dt, tzinfo)
        return calendar.timegm(dt_tz.utctimetuple())


    # Difference between the class method and the staticmethod
    # https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
    @classmethod
    def dt2UTCtimestamp(cls, dt: datetime.datetime) -> int:
        """
        by given a native time (UTC), the string of utc timestamp of timezone Europe/Berlin is returned

        Example usage:

        datetime_now = datetime.datetime.now()

        timestamp_now: int = TimeUtil.dt2UTCtimestamp(datetime_now)

        str_now = 'the datetime is {0}'.format(str(timestamp_now))
        # str(int) convert int to str

        print(str_now) # gives 1557330093 as in secs
        """
        return cls.dt2UTCtimestampWithTz(dt, 'Europe/Berlin')



