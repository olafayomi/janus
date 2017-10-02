#!/usr/bin/env python
#-*- coding:utf-8 -*-

import logging
import logging.handlers
import os
import signal
import sys
from functools import wraps
import yaml

def get_logger(logname, logfile, loglevel=logging.DEBUG, propagate=1):
    logger = logging.getLogger(logname)
    logFileHandler = logging.handlers.WatchedFileHandler(logfile)
    log_format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    formatter = logging.Formatter(log_format, '%b %d %H:%M:%S')
    logFileHandler.setFormatter(formatter)
    logger.addHandler(logFileHandler)
    logger.propagate = propagate
    logger.setLevel(loglevel)
    return logger

def load_config(config_file, logname, logfile):
    conflogger = get_logger(logname, logfile)
    try:
        with open(config_file, 'r') as stream:
            conf = yaml.safe_load(stream)
    except yaml.YAMLError as ex:
        conflogger.error('Error in file %s (%s)', config_file, str(ex))
        return None
    return conf

def kill_on_exception(logname):
    def _koe(func):
        @wraps(func)
        def __koe(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                logging.getLogger(logname).exception(
                    'Unhandled exception, killing RYU')
                logging.shutdown()
                os.kill(os.getpid(), signal.SIGTERM)
        return __koe
    return _koe

