import unittest
from parameterized import parameterized
from systems.standardSystem import StandardSystem


class StandardSystemTests(unittest.TestCase):
    @parameterized.expand([
        ["name"],
        ["1"],
    ])
    def test_name_is_set_as_in_constructor(self, name: str):
        # act
        model: StandardSystem = StandardSystem(name)

        # assert
        self.assertEqual(model.name, name)


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()