import unittest
import os.path
import Includer
class TestIncluder(unittest.TestCase):
#    def __init__(self):
#        pass
    def test_plus2plus(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [3, 6]
        answer = """class MyClass(object):
    def __init__(self):
        pass
    def Show(self):"""
        text = c.Include(path, lines=lines)
        self.assertEqual(text, answer)

    def test_all_none(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = None
        answer = """#!python3
#encoding: utf-8
class MyClass(object):
    def __init__(self):
        pass
    def Show(self):
        print('this is MyClass.')


if __name__ == '__main__':
    c = MyClass()
    c.Show()
"""
        text = c.Include(path, lines=lines)
        self.assertEqual(text, answer)

    def test_all_zero(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [0, 0]
        answer = """#!python3
#encoding: utf-8
class MyClass(object):
    def __init__(self):
        pass
    def Show(self):
        print('this is MyClass.')


if __name__ == '__main__':
    c = MyClass()
    c.Show()
"""
        text = c.Include(path, lines=lines)
        self.assertEqual(text, answer)

    def test_0_m5(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [0, -5]
        answer = """#!python3
#encoding: utf-8
class MyClass(object):
    def __init__(self):
        pass
    def Show(self):
        print('this is MyClass.')"""
        text = c.Include(path, lines=lines)
        self.assertEqual(text, answer)

    def test_5_2(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [5, 2]
        with self.assertRaises(Exception) as e:
            text = c.Include(path, lines=lines)
            self.assertEqual(e.msg, '引数linesは 左辺値 <= 右辺値 である必要があります。')

    def test_5_m2(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [5, -2]
        answer = """        pass
    def Show(self):
        print('this is MyClass.')


if __name__ == '__main__':"""
        text = c.Include(path, lines=lines)
        self.assertEqual(text, answer)

    def test_m5_2(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [-5, 2]
        with self.assertRaises(Exception) as e:
            text = c.Include(path, lines=lines)
            self.assertEqual(e.msg, '引数linesは 左辺値 <= 右辺値 である必要があります。')

    def test_m7_m2(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [-7, -2]
        answer = """        pass
    def Show(self):
        print('this is MyClass.')


if __name__ == '__main__':"""
        text = c.Include(path, lines=lines)
        self.assertEqual(text, answer)

    def test_7(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [7]
        with self.assertRaises(Exception) as e:
            text = c.Include(path, lines=lines)
            self.assertEqual(e.msg, '引数linesはlist型で[start, end]の2つの整数値を指定してください。0を指定するとstartは1, endは最終行数になります。負数を指定すると末尾からの行数です。-1なら最終行-1行目を指定します。')

    def test_none_none(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [None, None]
        with self.assertRaises(Exception) as e:
            text = c.Include(path, lines=lines)
            self.assertEqual(e.msg, '引数linesはlist型で[start, end]の2つの整数値を指定してください。0を指定するとstartは1, endは最終行数になります。負数を指定すると末尾からの行数です。-1なら最終行-1行目を指定します。')

    def test_1_none(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [1, None]
        with self.assertRaises(Exception) as e:
            text = c.Include(path, lines=lines)
            self.assertEqual(e.msg, '引数linesはlist型で[start, end]の2つの整数値を指定してください。0を指定するとstartは1, endは最終行数になります。負数を指定すると末尾からの行数です。-1なら最終行-1行目を指定します。')

    def test_none_8(self):
        c = Includer.Includer()
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '0.py')
        lines = [None, 8]
        with self.assertRaises(Exception) as e:
            text = c.Include(path, lines=lines)
            self.assertEqual(e.msg, '引数linesはlist型で[start, end]の2つの整数値を指定してください。0を指定するとstartは1, endは最終行数になります。負数を指定すると末尾からの行数です。-1なら最終行-1行目を指定します。')

