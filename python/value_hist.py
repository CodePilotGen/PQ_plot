#!/usr/bin/env python
#
# Copyright 2014 I.Sultanov
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,


from plotter_base import *
class value_hist(plotter_base):
    def __init__(self, label="", *args):
        plotter_base.__init__(self, blkname="value_hist", label=label, *args)
        self.message_port_register_in(pmt.intern("reals"));
        self.set_msg_handler(pmt.intern("reals"), self.handler);

        # set up curves
        curve = Qwt.QwtPlotCurve("x(n)");
        curve.attach(self);
        self.curves.append(curve);
        curve.setPen( Qt.QPen(Qt.Qt.green) );
        
        self.curve_data = [([],[])]
        self.hist = [];

    def handler(self, msg):
        # get input
        x = float(pmt.to_python(msg))
        self.hist.append(x);
        (density, domain) = numpy.histogram(self.hist,100);

        # pass data
        self.curve_data[0] = (domain, density);

        # trigger update
        self.emit(QtCore.SIGNAL("updatePlot(int)"), 0)


