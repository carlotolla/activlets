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
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
        sys.exit(0)

    def onButtonPressed(self, button):
        print("Hello World!")


def update_image(image_area, data=None):

    # remove the previous image
    for child in image_area.get_children():
        image_area.remove(child)

    # add a new image
    image = Gtk.Image()
    image.set_from_file("abudabi.jpg")
    image_area.add(image)
    image_area.show_all()


def main():
    builder = Gtk.Builder()
    builder.add_from_file("track.glade")
    builder.connect_signals(Handler())
    window = builder.get_object("applicationwindow1")
    viewport = builder.get_object("viewport1")
    viewport.connect("draw", update_image)
    window.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
