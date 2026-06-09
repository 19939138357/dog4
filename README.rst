Dogpile Cache Workbench
=======================

Dogpile Cache Workbench is a standalone repository edition of the dogpile
caching toolkit. It keeps the compact cache-region API and dogpile lock model
while giving this checkout its own project identity, repository metadata, and
workbench branding.

Local changes in this edition:

* Upstream project links were replaced with this standalone repository.
* Runtime branding is available from ``dogpile.WORKBENCH_NAME`` and
  ``dogpile.WORKBENCH_VERSION``.
* The git history is rebuilt from this snapshot so upstream branches do not
  appear automatically.

Dogpile consists of two subsystems, one building on top of the other.

``dogpile`` provides the concept of a "dogpile lock", a control structure
which allows a single thread of execution to be selected as the "creator" of
some resource, while allowing other threads of execution to refer to the previous
version of this resource as the creation proceeds; if there is no previous
version, then those threads block until the object is available.

``dogpile.cache`` is a caching API which provides a generic interface to
caching backends of any variety, and additionally provides API hooks which
integrate these cache backends with the locking mechanism of ``dogpile``.

Overall, dogpile.cache is intended as a replacement to the `Beaker
<https://pypi.org/project/Beaker/>`_ caching system, the internals of which are
written by the same author.   All the ideas of Beaker which "work" are re-
implemented in dogpile.cache in a more efficient and succinct manner, and all
the cruft (Beaker's internals were first written in 2005) relegated to the
trash heap.

Documentation
-------------

See the inherited documentation in ``docs/build`` and the local conversion
notes in ``WORKBENCH_NOTES.md``. The sections below provide a brief synopsis of
the ``dogpile`` packages.

Features
--------

* A succinct API which encourages up-front configuration of pre-defined
  "regions", each one defining a set of caching characteristics including
  storage backend, configuration options, and default expiration time.
* A standard get/set/delete API as well as a function decorator API is
  provided.
* The mechanics of key generation are fully customizable.   The function
  decorator API features a pluggable "key generator" to customize how
  cache keys are made to correspond to function calls, and an optional
  "key mangler" feature provides for pluggable mangling of keys
  (such as encoding, SHA-1 hashing) as desired for each region.
* The dogpile lock, first developed as the core engine behind the Beaker
  caching system, here vastly simplified, improved, and better tested.
  Some key performance
  issues that were intrinsic to Beaker's architecture, particularly that
  values would frequently be "double-fetched" from the cache, have been fixed.
* Backends implement their own version of a "distributed" lock, where the
  "distribution" matches the backend's storage system.  For example, the
  memcached backends allow all clients to coordinate creation of values
  using memcached itself.   The dbm file backend uses a lockfile
  alongside the dbm file.  New backends, such as a Redis-based backend,
  can provide their own locking mechanism appropriate to the storage
  engine.
* Writing new backends or hacking on the existing backends is intended to be
  routine - all that's needed are basic get/set/delete methods. A distributed
  lock tailored towards the backend is an optional addition, else dogpile uses
  a regular thread mutex. New backends can be registered with dogpile.cache
  directly or made available via setuptools entry points.
* Included backends feature three memcached backends (python-memcached, pylibmc,
  bmemcached), a Redis backend, a backend based on Python's
  anydbm, and a plain dictionary backend.
* Space for third party plugins, including one which provides the
  dogpile.cache engine to Mako templates.


Standalone Project Notes
------------------------

This edition is maintained as ``dogpile-cache-workbench`` at
https://github.com/19939138357/dogpile-cache-workbench.

Development / Bug reporting / Pull requests
___________________________________________

Use this repository's issue tracker for workbench-specific changes:
https://github.com/19939138357/dogpile-cache-workbench/issues.

Code of Conduct
_______________

Keep communication polite, thoughtful, and constructive.

License
-------

Dogpile is distributed under the `MIT license
<https://opensource.org/licenses/MIT>`_.
