"""
Created on Jun 22, 2014

@author: nhanitvn
"""
from __future__ import unicode_literals
import unittest
import pandas as pd

import test_base
from ddf import DistributedDataFrame


class TestDDF(test_base.BaseTest):

    def testDDFBasic(self):
        self.assertEqual(self.airlines.nrow, 31)
        self.assertEqual(self.airlines.ncol, 29)
        self.assertEqual(len(self.airlines), 31)

    def testSummary(self):
        df = self.airlines.summary()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df.columns), self.airlines.ncol)

    def testSample(self):
        df = self.airlines.head(10)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df.columns), self.airlines.ncol)
        self.assertItemsEqual(df.columns.tolist(), self.airlines.colnames)
        self.assertEqual(len(df), 10)

        df = self.airlines.sample(10, replacement=False)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df.columns), self.airlines.ncol)
        self.assertItemsEqual(df.columns.tolist(), self.airlines.colnames)
        self.assertEqual(len(df), 10)

        df = self.airlines.sample(10, replacement=True)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df.columns), self.airlines.ncol)
        self.assertItemsEqual(df.columns.tolist(), self.airlines.colnames)
        self.assertEqual(len(df), 10)

    def testSample2DDF(self):
        ddf2 = self.airlines.sample2ddf(0.5)
        self.assertIsInstance(ddf2, DistributedDataFrame)
        self.assertItemsEqual(ddf2.colnames, self.airlines.colnames)

    def testFiveNums(self):
        df = self.airlines.five_nums()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 5)

    def testVar(self):
        tp = self.airlines.var(0)
        self.assertIsInstance(tp, tuple)
        self.assertEqual(len(tp), 2)

        tp = self.airlines.var('lateaircraftdelay')
        self.assertIsInstance(tp, tuple)
        self.assertEqual(len(tp), 2)

    def testDropNA(self):
        ddf2 = self.airlines.drop_na(axis='row')
        self.assertIsInstance(ddf2, DistributedDataFrame)
        self.assertEqual(ddf2.ncol, self.airlines.ncol)

        ddf2 = self.airlines.drop_na(axis='column')
        self.assertIsInstance(ddf2, DistributedDataFrame)
        self.assertEqual(ddf2.nrow, self.airlines.nrow)

        with self.assertRaises(ValueError):
            self.airlines.drop_na(axis='whatever')

if __name__ == '__main__':
    unittest.main()
