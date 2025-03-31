# Unified login idea

## Lock Screen Proxy

* A thin layer that is launched from the login manager before the desktop. It
  does basic lock/unlock functionality and masks the desktop's.
* As it runs as the parent of every desktop, it can manage lock events and know
  what is running as whom.
* If the user locks their machine, all desktops can be told to lock. So no
  lock-> ctrl+alt+fN to bypass the lock.
* If the user unlocks their desktop, and then switches with ctrl+alt+fN, it can
  send the unlock event so they don't have to type their password again (it has
  the latest lock/unlock message and can unlock if the last was an unlock and
  the latest message was an unlock)
* This can be used for RDP, Xen, and other things you might log in to.
* It will be session manager agnostic.

### Text mode lock screen

* When VTs start up, the lock screen service is ready to lock or unlock the text
  mode virtual terminals too.

### Windows in Linux

* Set up KVM with GPU passthrough for dedicated Windows VM.
  * When launching it, check apps GPU unbinding and re-binding efficiently.
  * If the GPU isn't available, use a fallback.
* Make a viewer that starts with VNC, and extends/works with the lock manager
  from above.
* When there's a VM with GPU, switch VNC for Looking Glass so we can play games
  in Windows.
* Automate session management on both sides so locking/unlocking Windows
  cascades to Linux sessions too.

### RDP

* Lock/unlock events for RDP too.

## Notes from claude

### Primary Desktop Environments and Their Lock Signals

#### Desktop environments

- GNOME: Uses org.freedesktop.login1.Session.Lock() + org.gnome.ScreenSaver.Lock()
- KDE Plasma: Uses org.freedesktop.login1.Session.Lock() + org.freedesktop.ScreenSaver.Lock()
- XFCE: Uses org.freedesktop.ScreenSaver.Lock() through xfce4-screensaver
- Cinnamon: Uses org.freedesktop.ScreenSaver.Lock() + cinnamon-screensaver specific signals
- MATE: Uses org.freedesktop.ScreenSaver.Lock() through mate-screensaver
- LXQt: Uses org.freedesktop.ScreenSaver.Lock() through lxqt-screensaver
- Budgie: Uses GNOME's signals (org.gnome.ScreenSaver.Lock())
- Enlightenment (E): Custom signals through enlightenment_remote
- LXDE: Uses org.freedesktop.ScreenSaver.Lock() through light-locker or xscreensaver
- Deepin DE: Uses own com.deepin.SessionManager.Lock() + freedesktop signals
- Pantheon (Elementary): Uses GNOME's signaling system
- Unity: Uses GNOME's signaling system (largely historical now)

#### Methods

* The freedesktop standard signals (most universal)
* logind signals (for systemd systems)
* DE-specific signals for complete coverage

#### Window Managers

- i3/Sway: Typically use external lockers (i3lock/swaylock) without direct signals
- AwesomeWM: No built-in signals, relies on external lockers
- bspwm: No built-in signals, relies on external lockers
- DWM: No built-in signals, relies on external lockers

#### Common External Lock Managers

- light-locker: Uses org.freedesktop.ScreenSaver.Lock()
- xscreensaver: Legacy X11 locking mechanisms + some DBus support
- i3lock: Direct X11 locking, no signals
- swaylock: Direct Wayland locking, no signals

### Display Managers

* GDM (GNOME Display Manager)
* SDDM (Simple Desktop Display Manager)
* LightDM
* XDM (X Display Manager)
* LXDM
* SLiM
