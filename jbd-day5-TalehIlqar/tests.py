import unittest
from main import *

class Test(unittest.TestCase):
    def test_kub_funk(self):
            self.assertEqual(kub_funk(7),343)
            self.assertRaises(TypeError, kub_funk, 'string') #bu error ishlemir

            
   
    def test_Task_2(self):
        self.assertEqual(Task_2('a'), ['alma', 'proqramçı'])
        self.assertRaises(TypeError, Task_2, int) #bu error ishlemir
        


    def setUp(self) -> None:
        self.person = Person('koroglu', 'mirzeyev')
        return super().setUp()
    
    def test_person(self):
        self.assertEqual(self.person.get_fullname(), 'Koroglu Mirzeyev')
        self.assertIsInstance(self.person,Person)
    


if __name__ == '__main__':
    unittest.main()



        