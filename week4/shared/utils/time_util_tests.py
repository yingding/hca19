# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from timeutil import TimeUtil
import datetime as dt

# utc time now
now = dt.datetime.now()
# now_timestamp_local = 1557481029 + (2 * 3600); # with 2 hours ahead of time from germany for testing purpose
# now = dt.datetime.utcfromtimestamp(now_timestamp_local)

print(now.tzinfo)
print(now)
print(now.timestamp())

# Make the datetime timezone aware.
# german timezone: gt
print("\nWith Timezone:")
now_gt = TimeUtil.dt2dtWithTz(now, "Europe/Berlin")
print(now_gt.tzinfo)
print(now_gt)
print(now_gt.timestamp())

# convert the a timezone not aware datetime object
# to utc timestamp in secs
print("\nUTC timestamp:")
timestamp = TimeUtil.dt2UTCtimestamp(now)
print(timestamp)

# convert for a utc timestamp in secs int object
# to a german timezone datetime object
datetime_gt = TimeUtil.utcTimestamp2dt(timestamp)
print(datetime_gt.tzinfo)
print(datetime_gt)


"""
test begin timestamp of segment
"""
# test with 0 sec timeshift
timeshift = 0
seg = TimeUtil.get_segment_by_timestamp(timestamp) # use default 0
print("\nBegin Timestamp of {0} with {1} secs timeshift is {2}".format(timestamp, timeshift, seg.begin))
print("timestamp {} is the time {}".format(seg, TimeUtil.utcTimestamp2dt(seg.begin)))
print("\nEnd   Timestamp of {0} with {1} secs timeshift is {2}".format(timestamp, timeshift, seg.end))
print("timestamp {} is the time {}".format(seg, TimeUtil.utcTimestamp2dt(seg.end)))

# test with 5 min timeshift
timeshift = 300
seg = TimeUtil.get_segment_by_timestamp(timestamp, timeshift=timeshift)
print("\nBegin Timestamp of {0} with {1} secs timeshift is {2}".format(timestamp, timeshift, seg.begin))
print("timestamp {} is the time {}".format(seg, TimeUtil.utcTimestamp2dt(seg.begin)))
print("\nEnd   Timestamp of {0} with {1} secs timeshift is {2}".format(timestamp, timeshift, seg.end))
print("timestamp {} is the time {}".format(seg, TimeUtil.utcTimestamp2dt(seg.end)))

# test with 2 min timeshift with 5 min interval
timeshift = 120
interval = 300
seg = TimeUtil.get_segment_by_timestamp(timestamp, timeshift, interval)
print("\nBegin Timestamp of {0} with {1} secs timeshift is {2}".format(timestamp, timeshift, seg.begin))
print("timestamp {} is the time {}".format(seg, TimeUtil.utcTimestamp2dt(seg.begin)))
print("\nEnd   Timestamp of {0} with {1} secs timeshift is {2}".format(timestamp, timeshift, seg.end))
print("timestamp {} is the time {}".format(seg, TimeUtil.utcTimestamp2dt(seg.end)))

# test begin seg method
timeshift = 0
begin_timestamp = TimeUtil.segment_begin_by_timestamp(timestamp)
print("\nBegin Timestamp of {0} with {1} secs timeshift is {2}".format(timestamp, timeshift, begin_timestamp))

timeshift = 300
begin_timestamp = TimeUtil.segment_begin_by_timestamp(timestamp, )
print("\nBegin Timestamp of {0} with {1} secs timeshift is {2}".format(timestamp, timeshift, begin_timestamp))


