Notes (25 Dec 2017)

Right now, Mayavi doesn't work because pyface doesn't support Qt5. Everything
has been setup (including VTK) for Qt5. Changing things for Qt4 is possible,
but would be annoying. Far better to simply wait for Qt5 support.

The timeline for this seems pretty good right now, because Qt5 support was
merged into pyface/master on 24 Mar 2017. But the latest release of pyface as
of this writing is 5.1.0, which was released Apr 2016.

So in fact, experimental Qt5 support is possible by installing pyface master.
This is probably easy enough to do via pip, but I'm not too keen.
