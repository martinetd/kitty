#!/usr/bin/env python
# vim:fileencoding=utf-8
# License: GPL v3

from . import BaseTest
from kitty.fast_data_types import DECAWM, IRM, Cursor, DECCOLM, DECOM



class TestHistory(BaseTest):

    def test_history_short(self):
        s = self.create_screen()

        for i in range(1, 1000*1000):
            s.draw('aaa')
            s.linefeed()
            s.carriage_return()

    def test_history_long(self):
        s = self.create_screen()

        for i in range(1, 1000*200):
            s.draw('a' * 5 * 50)
            s.linefeed()
            s.carriage_return()
