from solution import TabularArray
import unittest


class TestTabularArray(unittest.TestCase):

    def test_convert_cell_to_list_1(self):
        A = [2,289,33,29,900280,3,22,4,100,9,8]
        number = 280
        K = None
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.convert_cell_to_list(number),[' ', ' ', ' ', '2', '8', '0',"|"])

    def test_convert_cell_to_list_2(self):
        A = [2,289,33,29,900280,3,22,4,100,9,8]
        number = 98700
        K = None
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.convert_cell_to_list(number), [' ', '9', '8', '7', '0', '0',"|"])

    def test_convert_cell_to_list_3(self):
        A = [2,289,33,29,900280,3,22,4,100,9,8]
        number = 876
        K = 6
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.convert_cell_to_list(number), [' ', ' ', ' ','8', '7', '6', "|"])

    def test_draw_row_1(self):
        A = [2,289,33,29,90028,3,22,4,100,9,8]
        K = 4
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.draw_number(), "|xxxxx|xxxxx|xxxxx|xxxxx|")

    def test_draw_row_2(self):
        A = [2,289,33,29,9002,3,22,4,100,9,8]
        K = 5
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.draw_number(), "|xxxx|xxxx|xxxx|xxxx|xxxx|")

    def test_draw_separator_1(self):
        A = [2,289,33,29,9002,3,22,4,100,9,8]
        K = 5
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.draw_separator(), "+----+----+----+----+----+")

    def test_draw_separato_2(self):
        A = [2,289,33,29,90028,3,22,4,100,9,8]
        K = 4
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.draw_separator(), "+-----+-----+-----+-----+")

    def test_number_of_lines(self):
        A = [2,289,33,29,90028,3,22,4,100,9,8,22,43,53] # 14
        K = 4
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.number_of_lines(), 9)

    def test_number_of_lines(self):
        A = [2,289,33,29,90028,3,22,4,100,9,8,22,43] # 13
        K = 3
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.number_of_lines(), 11)

    def test_number_of_lines(self):
        A = [2,289,33,29,90028,3,22,4,100,9] # 10
        K = 4
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.number_of_lines(), 7)

    def test_number_of_lines(self):
        A = [2,289,33,29,90028,3,22,4,100,9] # 10
        K = 5
        tabular_array = TabularArray(A,K)
        self.assertEqual(tabular_array.number_of_lines(), 5)


if __name__ == "__main__":
    unittest.main()
