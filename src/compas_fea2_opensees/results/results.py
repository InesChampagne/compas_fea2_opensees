from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import pickle
from pathlib import Path
from time import time
from subprocess import Popen
from subprocess import PIPE

from compas_fea2.results import Results, StepResults
from .read_results import get_data


class OpenseesResults(Results):

    def __init__(self, database_name, database_path, fields='all', steps='all', sets=None, output=True, components=None, exe=None, license='research',):
        super(OpenseesResults, self).__init__(database_name, database_path, fields, steps, sets, components, output)
        raise NotImplementedError

    # ==========================================================================
    # Extract results
    # ==========================================================================

    def extract_data(self):
        """Extract data from the Opensees .odb file.

        Returns
        -------
        None

        """
        raise NotADirectoryError()


class OpenseesStepResults(StepResults):
    def __init__(self, step, model, name=None):
        super(OpenseesStepResults, self).__init__(step, model, name)
