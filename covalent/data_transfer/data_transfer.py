# Copyright 2021 Agnostiq Inc.
#
# This file is part of Covalent.
#
# Licensed under the GNU Affero General Public License 3.0 (the "License").
# A copy of the License may be obtained with this software package or at
#
#      https://www.gnu.org/licenses/agpl-3.0.en.html
#
# Use of this file is prohibited except in compliance with the License. Any
# modifications or derivative works of this file must retain this copyright
# notice, and modified files must contain a notice indicating that they have
# been altered from the originals.
#
# Covalent is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the License for more details.
#
# Relief from the License may be granted by purchasing a commercial license.


import os
import pickle as _pickle
from pathlib import Path
from typing import List, Optional, Union

import cloudpickle as pickle
from werkzeug.datastructures import FileStorage

from .._shared_files import logger
from .._shared_files.config import get_config

app_log = logger.app_log
log_stack_info = logger.log_stack_info


def transfer(
    upload: FileStorage = None, dispatch_id: str = None, results_dir: str = None
) -> Union[FileStorage, bool]:
    """This function manages uploading and downloading data.

    Args:
        upload: A file that you want to upload.
        dispatch_id: The ID of the dispatch result you want to download.
        results_dir: The directory where results are stored.

    Returns:
        True if upload successful, results file if download successful, false otherwise.
    """
