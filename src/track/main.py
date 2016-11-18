#! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa Activlets
# Copyright 2013-2015 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# Activlets é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>

"""
O módulo aktask propõe um modelo de acesso a atividades ligadas a issues do github.

"""
import gi
import sys
import cairo

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk


class MouseButtons:

    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3


class Feature:
    def __init__(self, builder,  prefix):
        self.min, self.max, self.color_min, self.color_max = [
            builder.get_object("adjust_%s_%s%s" % (prefix, suffix, postfix))
            for postfix in ",_color".split(",") for suffix in "min max".split() ]
        self.min_color = self.color_min.get_rgba()
        self.max_color = self.color_max.get_rgba()


class Handler:
    def __init__(self, builder):

        self.statusbar = builder.get_object("statusbar1")
        # self.image = builder.get_object("image1")
        self.image = builder.get_object("drawingarea1")
        self.track = Feature(builder=builder, prefix="track")
        self.image.connect("draw", self.on_draw)
        # self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        h = 600  # self.image.get_height()
        w = 800  # self.image.get_width()
        rw = Gdk.get_default_root_window()
        # self.pixbuf = Gdk.pixbuf_get_from_window(rw, 0, 0, w, h)
        self.pixbuf = GdkPixbuf.Pixbuf.new_from_file("abudabi.jpg")
        # self.pixbuf = GdkPixbuf.Pixbuf.new(GdkPixbuf.Colorspace.RGB, False, 8, w, h)
        # self.pixbuf = Gdk.pixbuf_get_from_surface(rw, 0, 0, w, h)
        # self.pixbuf = self.image.get_pixbuf()
        self.pixarray = self.pixbuf.get_pixels()
        self.coords = []

        class Offset:
            y = self.pixbuf.get_rowstride()
            x = self.pixbuf.get_n_channels()
        self.offset = Offset
        self.context_id = self.statusbar.get_context_id("example")
        self.statusbar.push(self.context_id, "track color: %s" % self.track.min_color.to_string())

    @staticmethod
    def on_delete_window(*args):
        Gtk.main_quit(*args)
        sys.exit(0)

    def image_click(self, event, view=None):
        pass

    def on_draw(self, widget, cr=None):
        Gdk.cairo_set_source_pixbuf(cr, self.pixbuf, 0, 0)
        cr.paint()
        cr.set_source_rgb(0, 0, 0)
        cr.set_line_width(0.5)

        for i in self.coords:
            for j in self.coords:

                cr.move_to(i[0], i[1])
                cr.line_to(j[0], j[1])
                cr.stroke()

        del self.coords[:]
        pass

    def on_image_click(self, target, event, view=None):
        pixel = self.pixarray[int(event.x * self.offset.x + event.y * self.offset.y)]
        pixelg = self.pixarray[int(event.x * self.offset.x + 1 + event.y * self.offset.y)]
        pixelb = self.pixarray[int(event.x * self.offset.x + 2+ event.y * self.offset.y)]
        self.statusbar.push(self.context_id, "x: %d, y: %d, pixel: %s, pixel: %s, pixel: %s"
                            % (event.x, event.y, pixel, pixelg, pixelb))
        if event.type == Gdk.EventType.BUTTON_PRESS \
            and event.button == MouseButtons.LEFT_BUTTON:

            self.coords.append([event.x, event.y])

        if event.type == Gdk.EventType.BUTTON_PRESS \
            and event.button == MouseButtons.RIGHT_BUTTON:

            self.image.queue_draw()

    def track_scan(self):
        tolerance, xr, xg, xb = \
            self.track.min, self.track.min_color.red, self.track.min_color.green, self.track.min_color.blue
        for y in range(200, 600):
            for x in range(200):
                r, g, b = [self.pixarray[int(x * self.offset.x + channel + y * self.offset.y)] for channel in (0, 1, 2)]
                match = abs(xr - r) < tolerance and abs(xg - g) < tolerance and abs(xb - b) < tolerance


def update_image(image_area, data=None):
    return

    # remove the previous image
    for child in image_area.get_children():
        image_area.remove(child)
    pixbuf = GdkPixbuf.Pixbuf.new_from_file("abudabi.jpg")
    image = Gtk.Image.new_from_pixbuf(pixbuf)
    # add a new image
    # image = Gtk.Image()
    # image.set_from_file("abudabi.jpg")
    image_area.add(image)
    image_area.show_all()


def main():
    builder = Gtk.Builder()
    builder.add_from_file("track.glade")
    builder.connect_signals(Handler(builder))
    window = builder.get_object("applicationwindow1")
    viewport = builder.get_object("viewport1")
    viewport.connect("draw", update_image)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
