"""
debug_log.py
This file provides DebugLog class,
the wrapper to logging.Logger.
This class creates the logger which is already configured to:
 - write formatted messages to stderr
 - write formatted messages to Windows event log
 - write formatted messages to Linux syslog
 - write formatted messages to file
2020-05-22
"""
__author__ = 'shmakovpn <shmakovpn@yandex.ru>'
__date__ = '2020-05-22'

import os
import sys
import logging
import logging.handlers
from typing import Optional, Dict


class DebugLog:
    """
    This class is a wrapper for logging.Logger.

    Requirements:
        Windows:
            pip install pywin32
            Run at once to create the registry key. Then give full rights on the registry key to user manually

    Notes:
        Linux: do not use logger.debug(msg) with syslog

    Usage:
    >>> logger: DebugLog = DebugLog(
    ... logger_name=os.path.basename('my_log'),
    ... log_file_path='./my.log',
    ... syslog=False,
    ... stderr=True,
    ... level=logging.DEBUG,
    ... )

    2020-05-21
    """
    LEVELS: Dict[int, str] = {
        logging.DEBUG: 'DEBUG',
        logging.INFO: 'INFO',
        logging.WARNING: 'WARNING',
        logging.ERROR: 'ERROR',
        logging.CRITICAL: 'CRITICAL',
    }
    """Supported levels of logging"""

    def __init__(self, logger_name: str,
                 log_file_path: Optional[str] = None,
                 syslog: Optional[bool] = None,
                 stderr: Optional[bool] = None,
                 level: int = logging.DEBUG):
        """
        Constructor
        :param logger_name: the name of the logger
        :type logger_name: str
        :param log_file_path: the path to log file, if None logging to file will be disabled
        :type log_file_path: str
        :param syslog: if True logging to syslog (under Linux) or to event log (under Windows) will be enabled
        :type syslog: bool
        :param  stderr: if True log messages will be copied to STDERR too
        :type stderr: bool
        :param level: the level of logging
        :type level: int
        """
        self.logger_name = logger_name
        self.log_file_path: Optional[str] = log_file_path
        self.syslog: Optional[bool] = syslog
        self.stderr: Optional[bool] = stderr
        self.level: int = level
        # create new logger
        self.logger: logging.Logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.level)
        # create new formatters
        self.file_formatter: logging.Formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.syslog_formatter: logging.Formatter = logging.Formatter(
            '%(name)s - %(levelname)s - %(message)s'
        )
        # create file_handler if need
        if self.log_file_path:
            self.file_handler: Optional[logging.handlers.RotatingFileHandler] = logging.handlers.RotatingFileHandler(
                filename=self.log_file_path,
                maxBytes=1024*1024,
                backupCount=5,
            )
            self.file_handler.setFormatter(self.file_formatter)
            self.logger.addHandler(self.file_handler)
        else:
            self.file_handler: Optional[logging.handlers.RotatingFileHandler] = None
        # create syslog of event handler
        self.syslog_handler: Optional[logging.handlers.SysLogHandler] = None
        self.event_handler: Optional[logging.handlers.NTEventLogHandler] = None
        if self.syslog:
            if os.name == 'nt':
                self.event_handler: Optional[logging.handlers.NTEventLogHandler] = logging.handlers.NTEventLogHandler(
                    appname=self.logger_name
                )
                self.logger.addHandler(self.event_handler)
            elif os.name == 'posix':
                self.syslog_handler: Optional[logging.handlers.SysLogHandler] = logging.handlers.SysLogHandler(
                    '/dev/log'
                )
                self.syslog_handler.setFormatter(self.syslog_formatter)
                self.syslog_handler.setLevel(self.level)
                self.logger.addHandler(self.syslog_handler)
            else:
                raise RuntimeError(f"Could not create a logger. Unsupported os type '{os.name}'")

    def _stderr(self, msg: str, level: int) -> None:
        """
        Formats msg, then writes it to stderr
        :param msg: log message
        :type msg: str
        :param level: log message level
        :type level: int
        :return: None
        """
        sys.stderr.write(f"{self.LEVELS[level]} - {msg}\n")

    def debug(self, msg: str) -> None:
        """
        Wrapper to logging.Logger.debug(msg)
        :param msg: log message
        :type msg: str
        :return: None
        """
        if self.level <= logging.DEBUG:
            self._stderr(msg, logging.DEBUG)
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        """
        Wrapper to logging.Logger.info(msg)
        :param msg: log message
        :type msg: str
        :return: None
        """
        if self.level <= logging.INFO:
            self._stderr(msg, logging.INFO)
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        """
        Wrapper to logging.Logger.warning(msg)
        :param msg: log message
        :type msg: str
        :return: None
        """
        if self.level <= logging.WARNING:
            self._stderr(msg, logging.WARNING)
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """
        Wrapper to logging.Logger.error(msg)
        :param msg: log message
        :type msg: str
        :return: None
        """
        if self.level <= logging.ERROR:
            self._stderr(msg, logging.ERROR)
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        """
        Wrapper to logging.Logger.critical(msg)
        :param msg: log message
        :type msg: str
        :return: None
        """
        if self.level <= logging.CRITICAL:
            self._stderr(msg, logging.CRITICAL)
        self.logger.error(msg)
