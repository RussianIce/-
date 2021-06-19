#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: QQQ
# Author: RUSSIAN ICE
# Generated: Sat Jun 19 15:06:20 2021
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class PAPICH(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="QQQ")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_check_box_0 = variable_check_box_0 = True
        self.sample_rate = sample_rate = 5E6
        self.RF = RF = 13
        self.CF = CF = 100000000

        ##################################################
        # Blocks
        ##################################################
        self._sample_rate_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.sample_rate,
        	callback=self.set_sample_rate,
        	label="Sample Rate: 1.024M, 1.4M, 1.8M, 1.92M, 2.048M, 2.4M & 2. 56M",
        	converter=forms.float_converter(),
        )
        self.GridAdd(self._sample_rate_text_box, 7, 0, 1, 5)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "RF")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "WATERFALL")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab3")
        self.GridAdd(self.notebook_0, 1, 0, 4, 5)
        _RF_sizer = wx.BoxSizer(wx.VERTICAL)
        self._RF_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_RF_sizer,
        	value=self.RF,
        	callback=self.set_RF,
        	label="RF Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._RF_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_RF_sizer,
        	value=self.RF,
        	callback=self.set_RF,
        	minimum=0,
        	maximum=45,
        	num_steps=45,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_RF_sizer, 6, 0, 1, 5)
        _CF_sizer = wx.BoxSizer(wx.VERTICAL)
        self._CF_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_CF_sizer,
        	value=self.CF,
        	callback=self.set_CF,
        	label="Center Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._CF_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_CF_sizer,
        	value=self.CF,
        	callback=self.set_CF,
        	minimum=80.9e6,
        	maximum=2400000000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_CF_sizer, 5, 0, 1, 5)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.notebook_0.GetPage(1).GetWin(),
        	baseband_freq=CF,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=sample_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Waterfall Plot",
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.notebook_0.GetPage(0).GetWin(),
        	baseband_freq=CF,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=sample_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        	size=(575,600),
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self._variable_check_box_0_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.variable_check_box_0,
        	callback=self.set_variable_check_box_0,
        	label='variable_check_box_0',
        	true=True,
        	false=False,
        )
        self.Add(self._variable_check_box_0_check_box)
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_0.set_sample_rate(sample_rate)
        self.rtlsdr_source_0.set_center_freq(CF, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(RF, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna("", 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
          
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=44100,
                decimation=250000,
                taps=None,
                fractional_bw=None,
        )
        self.low_pass_filter_0 = filter.fir_filter_ccf(20, firdes.low_pass(
        	1, sample_rate, 100000, 10000, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(44100, "", False)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=250000,
        	audio_decimation=1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_wfm_rcv_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.rtlsdr_source_0, 0), (self.wxgui_waterfallsink2_0, 0))    

    def get_variable_check_box_0(self):
        return self.variable_check_box_0

    def set_variable_check_box_0(self, variable_check_box_0):
        self.variable_check_box_0 = variable_check_box_0
        self._variable_check_box_0_check_box.set_value(self.variable_check_box_0)

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self._sample_rate_text_box.set_value(self.sample_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.sample_rate, 100000, 10000, firdes.WIN_HAMMING, 6.76))
        self.rtlsdr_source_0.set_sample_rate(self.sample_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.sample_rate)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.sample_rate)

    def get_RF(self):
        return self.RF

    def set_RF(self, RF):
        self.RF = RF
        self._RF_slider.set_value(self.RF)
        self._RF_text_box.set_value(self.RF)
        self.rtlsdr_source_0.set_gain(self.RF, 0)

    def get_CF(self):
        return self.CF

    def set_CF(self, CF):
        self.CF = CF
        self._CF_slider.set_value(self.CF)
        self._CF_text_box.set_value(self.CF)
        self.rtlsdr_source_0.set_center_freq(self.CF, 0)
        self.wxgui_fftsink2_0.set_baseband_freq(self.CF)
        self.wxgui_waterfallsink2_0.set_baseband_freq(self.CF)


def main(top_block_cls=PAPICH, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
