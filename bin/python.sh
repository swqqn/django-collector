#!/bin/sh

LNDLRD_HOME="$(dirname $0)"/..
export LNDLRD_HOME

. "${LNDLRD_HOME}"/etc/common

"${PYTHON}" ${PYTHONFLAGS} ${LNDLRD_PYTHONFLAGS} "$@"

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
