from __future__ import annotations

import gi
import sys

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, GLib

from .ui import MainWindow
from .i18n import _


class DnfAppCenter(Adw.Application):
    def __init__(self) -> None:
        super().__init__(application_id="org.dnf.AppCenter", flags=Gio.ApplicationFlags.HANDLES_OPEN)
        self._launch_updates = False
        self.add_main_option(
            "update",
            0,
            GLib.OptionFlags.NONE,
            GLib.OptionArg.NONE,
            _("Open directly to the Updates section"),
            None,
        )
        Adw.init()

    def do_handle_local_options(self, options) -> int:  # type: ignore[override]
        try:
            self._launch_updates = bool(options.contains("update"))
        except Exception:
            self._launch_updates = False
        return -1

    def do_activate(self) -> None:  # type: ignore[override]
        window = self.props.active_window
        if window is None:
            window = MainWindow(self, launch_updates=self._launch_updates)
        window.present()

    def do_open(self, files, _n_files: int, _hint: str) -> None:  # type: ignore[override]
        window = self.props.active_window
        if window is None:
            window = MainWindow(self, launch_updates=self._launch_updates)
        window.present()

        rpm_paths: list[str] = []
        for file in files:
            try:
                path = file.get_path()
            except Exception:
                path = None
            if path and path.lower().endswith('.rpm'):
                rpm_paths.append(path)

        if rpm_paths:
            window.queue_rpm_file_install(rpm_paths)
        else:
            self.activate()


def main() -> int:
    app = DnfAppCenter()
    return app.run(sys.argv)


if __name__ == "__main__":
    raise SystemExit(main())
