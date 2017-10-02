#!/usr/bin/env python
#-*- coding:utf-8 -*-

import utils

def get_vlans(config_file, logname, logfile):
    '''Return all VLANs in config file'''
    logger = utils.get_logger(logname, logfile)
    conf = utils.load_config(config_file, logname, logfile)
    
    if conf is not None:
        try:
            vlans = conf['vlans']
            return vlans
        except KeyError:
            logger.error("No VLANs included in config file")
    else:
        logger.error("No configuration in file!!!")

def get_dps(config_file, logname, logfile):
    '''Return all DPs in config file'''
    logger = utils.get_logger(config_file, logname, logfile)
    conf = utils.load_config(config_file, logname, logfile)

    if conf is not None:
        try:
            datapaths = conf['datapaths']
            return datapaths
        except KeyError:
            logger.error("No datapath included in config file")
    else:
        logger.error("No configuration in file!!!")

