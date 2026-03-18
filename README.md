# DNF App Center

DNF App Center is a GTK4/libadwaita package manager and updater for Fedora-family systems.
It uses AppStream for catalog metadata and libdnf5 for package state and transactions.

## Features

- Browse applications by category
- Search the full package/app catalog
- Install, remove, and update packages with transaction preflight checks
- Drag-and-drop or open local `.rpm` files for installation
- News page backed by a configurable update feed URL
- Background updater tray service with notifications and configurable intervals

## Commands

Main application:

```bash
DNF App Center
dnf-app-center
```

Open directly to the **Updates** page:

```bash
dnf-app-center --update
```

Updater service:

```bash
dnf-app-center-updater
```

Standalone update checks:

```bash
dnf-app-center-updater --check
dnf-app-center-updater --check --refresh
dnf-app-center-updater --check --json
```

Return codes for `--check`:

- `0` = no updates available
- `100` = updates available
- `2` = error

## Configuration

Per-user updater/news settings are stored in:

```text
~/.config/dnf-app-center/updater.json
```

Current keys:

- `enabled`
- `notifications`
- `interval_value`
- `interval_unit`
- `update_feed_url`

Example:

```json
{
  "enabled": true,
  "notifications": true,
  "interval_value": 12,
  "interval_unit": "hours",
  "update_feed_url": "https://updates.nobaraproject.org/updates.txt"
}
```

## Building locally

Install typical Fedora build dependencies:

```bash
sudo dnf builddep ./dnf-app-center.spec
```

Build an RPM from the source tarball/spec:

```bash
mkdir -p ~/rpmbuild/{SOURCES,SPECS}
cp dnf-app-center-*.tar.gz ~/rpmbuild/SOURCES/
cp dnf-app-center.spec ~/rpmbuild/SPECS/
rpmbuild -ba ~/rpmbuild/SPECS/dnf-app-center.spec
```

## Build options

The RPM spec supports overriding the default news/update feed URL at build time:

```bash
rpmbuild -ba dnf-app-center.spec --define '_update_feed_url https://example.com/updates.txt'
```

That value becomes the default `update_feed_url` used when the user has not overridden it in their own config.

## License

This project is distributed under the terms of the GNU General Public License version 2.
See `COPYING` for the full license text.
