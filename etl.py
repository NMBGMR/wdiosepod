# ===============================================================================
# Copyright 2020 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
import logging
from contextlib import contextmanager
from ftplib import FTP
from os import environ

from context import contextlock, ctx
from generate_yml import generate_yml

OSE_FTP_URL = 'ftp.ose.org'
OSE_FTP_USER = environ.get('OSE_FTP_USER')
OSE_FTP_PWD = environ.get('OSE_FTP_PWD')


@contextmanager
def ftpclient():
    ftp = None
    try:
        ftp = FTP(OSE_FTP_URL, timeout=3)
        ftp.login(OSE_FTP_USER, OSE_FTP_PWD)
    except BaseException as e:
        message('failed to connect')
        # import traceback
        # traceback.print_exc()

    try:
        yield ftp
    finally:
        if ftp is not None:
            ftp.quit()


def message(msg):
    print('message:  {}'.format(msg))
    with contextlock:
        if 'log' not in ctx:
            ctx['log'] = []

        ctx['log'].append(msg)
        ctx['message'] = msg


def etl():
    # download files for ftp
    try:
        with ftpclient() as clt:
            pass
    except RuntimeError:
        message('failed getting ftp client')

    pod = ''
    mi = ''
    mr = ''

    for obj in generate_yml(pod, mi, mr):
        # upload to the ose import dataset
        message('added object')

# ============= EOF =============================================
