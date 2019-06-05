import pprint # pretty print
import pandas as pd
from shared.dbhelper.dbfactory import DBFactory
from shared.dbhelper.accesshelper import AccessHelper
import json, os
from collections import namedtuple
from shared.utils.timeutil import TimeUtil
from pymongo.database import Database as Database
from shared.utils.plotutil import PlotUtil
import re  # RegEx
# import datetime

# Global variable
global config_file_name

config_file_name = "db_config.json"
# config_file_name = "db_config_filled.json"

"""
Section of helper methods
"""


def get_config_file_path() -> str:
    """this method returns the absolute file path of db_config.json file, where credentials are saved"""
    current_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_path)
    return os.path.join(current_dir, "shared", "dbhelper", config_file_name)


def convert(dictionary) -> namedtuple:
    """ convert a simple one depth dictionary object to a namedtuple object """
    # example of quick convert simple dictionary to named tuple: https://gist.github.com/href/1319371
    return namedtuple('GenericDict', dictionary.keys())(**dictionary)


def get_db() -> Database:
    """ this method returns a pymongo.database Database object """

    # get the absolute config file path
    config_file_path = get_config_file_path()

    # load json db config file
    with open(config_file_path, 'r', encoding="utf-8") as config_file:
        # json.load for file and json.loads for string
        config_dict = json.load(config_file)

    # convert the db config to a namedtuple object
    db_config = convert(config_dict)

    # Get a database object for remote mongodb database
    db = DBFactory.getDB(db_config.host,db_config.db,db_config.user,db_config.password)
    return db


def mood2idx(x: str) -> int:
    """
    this method maps a string of mood to a int code of mood
    :param x: string mood expression
    :return: mood code as int value
    """
    # any thing match J char just for fun
    # python regex intro https://www.w3schools.com/python/python_regex.asp
    if x == 'NOTHING' or re.match("J",x):
        return 0;
    elif x == 'SAD':
        return -1;
    elif re.match('^HA',x):
        return 1;
    else:
        return 0


def __main__():
    # get db connection
    db = get_db()

    # Application Run Section
    # show all collections in mongodb
    DBFactory.test(db)

    i = 0
    i += 1
    # get all entries of collection moods as a list
    print("\n#### Example {}: get all entries as a list".format(i))
    my_list = AccessHelper.get_collection_entries_as_list(db, "moods")
    pprint.pprint(my_list)

    # get all entries of collection moods as a dataframe
    i += 1
    print("\n#### Example {}: get all entries as a list".format(i))
    df = AccessHelper.get_collection_entries_as_dataframe(db, "moods")
    pprint.pprint(df)

    # get all entries as seleted dataframe
    start_timestamp = '1524599226551'
    end_timestamp = '1557398154843'
    # endTimestamp = datetime.datetime.now().timestamp()
    # endTimestamp = int(endTimestamp) * 1000
    # print("endTimestamp",  endTimestamp)
    i += 1
    print("\n#### Example {}: get all entries as seleted dataframe from {} to {}".format(i, start_timestamp, end_timestamp))
    df = AccessHelper.get_collection_entries_as_dataframe(db, "moods", start=start_timestamp, end=end_timestamp, col_name='_id.timestamp')
    pprint.pprint(df)

    # get all entries with mapper function
    i += 1
    print("\n#### Example {}: get all entries as seleted dataframe with mapper".format(i))
    mapper = lambda x: {'timestamp': x['_id']['timestamp'], 'mood': x['mood']}
    df = AccessHelper.get_collection_entries_as_dataframe(db, "moods",mapper=mapper)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    pprint.pprint(df)


    # get all entries with mapper function and timestamp as index
    i += 1
    print("\n#### Example {}: get all entries as seleted dataframe with mapper and timezone conversion".format(i))
    #format = '%Y-%m-%d %H:%M:%S.%f'
    #format = '%Y-%m-%d %H:%M:%S'
    # the timestamp from database are javascript timestamp which is given in miliseconds, it shall be converted to seconds.
    mapper = lambda x: {'timestamp': TimeUtil.utcTimestamp2dt(int(x['_id']['timestamp'])/1000), 'mood': x['mood']}
    df = AccessHelper.get_collection_entries_as_dataframe(db, "moods",mapper=mapper)
    pprint.pprint(df)

    # get all entries with mapper function and timestamp as index
    i += 1
    print("\n#### Example {}: get all entries as seleted dataframe with mapper and converted index to timestamp".format(i))
    df = AccessHelper.get_collection_entries_as_dataframe(db, "moods",mapper=mapper)
    ## set index of a dataframe
    ## https://stackoverflow.com/questions/10457584/redefining-the-index-in-a-pandas-dataframe-object
    # format = '%Y-%m-%d %H:%M:%S.%f'

    # df['timestamp'] = pd.to_datetime(df['timestamp'])
    AccessHelper.set_index_inplace(df, 'timestamp')
    df.sort_index(inplace=True, ascending=False)
    print(df)


    # Slicing the dataframe
    i += 1
    print("\n#### Example {}: get the 2nd to 6th rows of a dataframe".format(i))
    df_sliced = df.iloc[1:6, :] # first row slicing and then column slicing, since 6 is exlusive row index from 1 - 5 is selected.
    print(df_sliced)

    """Plotting"""

    # map the text to value codes for plotting
    mood_codes = [mood2idx(x) for x in df['mood'].tolist()]

    # pprint.pprint(mood_binary)
    # index2 = index.to_pydatetime().tolist()

    # style "bo" for blue dots
    PlotUtil.ploting(df.index, mood_codes, "time line", 'mood codes', 'categorical moods','b+','mood', True)


"""Run the main method"""
__main__()










