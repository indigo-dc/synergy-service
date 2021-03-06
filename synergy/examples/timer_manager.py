import logging
import time

from synergy.common.manager import Manager
from synergy.exception import SynergyError


__author__ = "Lisa Zangrando"
__email__ = "lisa.zangrando[AT]pd.infn.it"
__copyright__ = """Copyright (c) 2015 INFN - INDIGO-DataCloud
All Rights Reserved

Licensed under the Apache License, Version 2.0;
you may not use this file except in compliance with the
License. You may obtain a copy of the License at:

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.
See the License for the specific language governing
permissions and limitations under the License."""

LOG = logging.getLogger(__name__)


class TimerManager(Manager):

    def __init__(self):
        Manager.__init__(self, name="TimerManager")

    def setup(self):
        LOG.info("%s setup invoked!" % (self.name))

    def execute(self, command, *args, **kargs):
        LOG.info("%r execute %r invoked!" % (self.name, command))

        if command == "GET_TIME":
            return {"localtime": time.asctime(time.localtime(time.time()))}
        else:
            raise SynergyError("command %r not supported" % command)

    def destroy(self):
        LOG.info("%s destroy invoked!" % (self.name))

    def task(self):
        localtime = time.asctime(time.localtime(time.time()))
        LOG.info("Local current time: %s" % (localtime))
