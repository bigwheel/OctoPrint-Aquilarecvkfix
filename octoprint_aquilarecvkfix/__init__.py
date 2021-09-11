# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin


class AquilarecvkfixPlugin(ooctoprint.plugin.OctoPrintPlugin):
    # https://www.reddit.com/r/VoxelabAquila/comments/pj1x7x/a_print_with_octoprint_often_freezes_several/hc4x3hu/?
    # Recv: ok
    # Send: N3988 G1 X87.90 Y95.68 F4800*125
    # Recv:  T:199.77 /200.00 (109.50) B:60.3 /60.00 (855.00) @:0 B@:0
    # Recv: k
    def fix(self, comm_instance, line, *args, **kwargs):
        if line == "k":
            return "ok"
        else:
            return line


__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=3,<4"
__plugin_implementation__ = AquilarecvkfixPlugin()
__plugin_hooks__ = {
    "octoprint.comm.protocol.gcode.received": (__plugin_implementation__.fix, 1),
}
