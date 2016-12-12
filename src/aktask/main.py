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

NL = []
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Gio
MEDIA = {"": "⏣", "pendente": "⏹", "em execucao": "⏵", "pronto": "⏯", "pausado": "⏸", "completo": "⏏"}
MEDIAS = {"": "akissue", "pendente": "akpend", "em execucao": "akgo",
          "pronto": "akready", "pausado": "akpause", "completo": "akstop"}


class MainWindow(Gtk.Window):
    def __init__(self, builder):
        Gtk.Window.__init__(self, title="Activ Tasks")
        self._set_style()
        builder.add_from_file("aktask/aktask.glade")
        builder.connect_signals(self)
        self.set_size_request(800, 400)
        self.object_being_built = self
        self.build_stack = []
        self.stack_layer = builder.get_object("group_issues")
        window = builder.get_object("applicationwindow1")
        window.show_all()

    @staticmethod
    def on_delete_window(*args):
        Gtk.main_quit(*args)
        sys.exit(0)

    def _set_style(self):
        style_provider = Gtk.CssProvider()

        css = open('aktask/aktask.css', 'rb')  # rb needed for python 3 support
        css_data = css.read()
        css.close()

        style_provider.load_from_data(css_data)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION

        )

    def build(self, part=""):
        self.object_being_built.add(part)
        self.object_being_built = self.build_stack.pop() if self.build_stack else self.object_being_built

    def build_window(self, name=""):
        self.connect("destroy", self.on_delete_window)
        self.build_stack.append(self.listbox)

    def build_issue(self, **kwargs):
        lbl = GtkIssue(**kwargs)
        self.stack_layer.pack_start(lbl, False, False, 0)
        # self.build_stack.append(self.stack)

    def build_list(self, name=""):
        lbl = Gtk.Label(name, xalign=0.0)
        row = Gtk.ListBoxRow()
        row.add(lbl)
        self.listbox.add(row)
        self.stack.add_named(self.stack_layer, name)
        self.build_stack.append(self.stack)


from gi_composites import GtkTemplate


@GtkTemplate(ui='aktask/akissue.glade')
class GtkIssue(Gtk.Box):

    __gtype_name__ = 'issueboxer'

    # issue_title = GtkTemplate.Child()
    # issue_info = GtkTemplate.Child()
    issue_title, issue_info, rotulo, milestone_corrente, nivel_valor, nivel_urgencia,\
        nivel_prioridade, encarregado_0, number = GtkTemplate.Child.widgets(9)

    def __init__(self, title="", number=0, labels=NL, state="pendente", milestone="labase",
                 deadline="asap", assignee=NL, **kwargs):
        super(GtkIssue, self).__init__(orientation=Gtk.Orientation.VERTICAL, border_width=3)
        # This must occur *after* you initialize your base
        self.init_template()
        number_string = tuple("%03d" % number)
        self.number.set_text("- %s %s %s -" % number_string)
        self.issue_title.set_text("%s" % title)
        self.issue_info.set_text("%s %s" % (MEDIA[state], state))
        self.issue_info.get_style_context().add_class(MEDIAS[state])
        self.milestone_corrente.set_text(milestone)
        self.rotulo.set_text(labels[0] if labels else assignee[0] if assignee else "")
        self.encarregado_0.set_tooltip_text(assignee[0] if assignee else "")

    def ___init__(self, title="", number=0, labels=NL, state="pendente", **kwargs):
        super(GtkIssue, self).__init__(orientation=Gtk.Orientation.VERTICAL, border_width=3)
        label_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        lbl = Gtk.Label("%s - %d" % (title, number), xalign=0.0)

        self.pack_start(label_box, False, False, 0)
        label_box.pack_start(lbl, False, False, 0)
        for label in labels:
            lb = Gtk.Label(" %s " % label, xalign=0.0)
            label_box.pack_start(lb, False, False, 0)

        stat = Gtk.Label(" %s " % state, xalign=0.0)

        label_box.pack_start(stat, False, False, 0)
        self.progress = Gtk.ProgressBar()
        self.pack_start(self.progress, False, False, 0)


class Visitor:
    def __init__(self, gtk_builder):
        self.gtk_builder = gtk_builder

    def build_project(self, name=""):
        pass
        # self.gtk_builder.build_list(name)

    def build_issue(self, **kwargs):
        self.gtk_builder.build_issue(**kwargs)

    def update(self, **kwargs):
        return self.build_project(**kwargs) if len(kwargs) == 1 else self.build_issue(**kwargs)

    def visit(self, model):
        model.retrieve(self)


def main():

    # from aktask.control import MainControl
    from activ_factory import MainControl
    control = MainControl()
    control.fill_with_data()
    win = MainWindow(Gtk.Builder())
    control.render_data_to_gui(writer=Visitor(gtk_builder=win))
    Gtk.main()


if __name__ == '__main__':
    main()
