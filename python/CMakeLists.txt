# Copyright 2011 Free Software Foundation, Inc.
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


########################################################################
# Include python install macros
########################################################################
include(GrPython)
if(NOT PYTHONINTERP_FOUND)
    return()
endif()

########################################################################
# Install python sources
########################################################################
GR_PYTHON_INSTALL(
    FILES
    __init__.py
    pdu_lambda.py
    set_title.py
    stream_lambda.py
    const_plot.py
    ctime_plot.py
    raster_plot.py
    value_plot.py
    value_hist.py
    cpsd_plot.py
    time_plot.py
    time_hist.py
    cpower_plot.py
    plotter_base.py
    pdu_meta_extract.py
    text_input.py
    select_input.py
    variable_text_input.py
    range_input.py
    text_output.py
    meta_text_output.py
    head.py
    skip_head.py
    trim_tail.py
    file_message_source.py
    file_message_sink.py
    file_open.py
    dict_ui_source.py
    table.py DESTINATION ${GR_PYTHON_DIR}/pyqt
)

########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

set(GR_TEST_TARGET_DEPS gnuradio-pyqt)
set(GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/swig)
