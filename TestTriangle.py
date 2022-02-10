# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(7,24,25),'Right','7,24,25 is a Right triangle')
    def testRightTriangleD(self): 
        self.assertEqual(classifyTriangle(25,7,24),'Right','25,7,24 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(8,8,8),'Equilateral','8,8,8 should be equilateral')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(8,3,5),'Scalene','8,3,5 should be Scalene')
    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(7,3,7),'Scalene','7,3,7 should be Scalene')
    
    def testIsoscelesTrianglesA(self): 
        self.assertEqual(classifyTriangle(8,8,3),'Isosceles','8,8,3 should be Isosceles')
    def testIsoscelesTrianglesB(self): 
        self.assertEqual(classifyTriangle(6,4,6),'Isosceles','6,4,6 should be Isosceles')
    
    


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

