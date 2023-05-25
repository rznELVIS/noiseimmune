import unittest
from infrastructure.options import Options
from parameterized import parameterized
from systems.standardSystem import StandardSystem


class StandardSystemTests(unittest.TestCase):
    @parameterized.expand([
        ["name"],
        [""]
    ])
    def test_name_is_set_as_in_constructor(self, name: str):
        # act
        model: StandardSystem = StandardSystem(name)

        # assert
        self.assertEqual(model.name, name)

    @parameterized.expand([
        [0],
        [1],
        [100]
    ])
    def test_go_is_executed_without_error(self, count: int):
        # arrange
        model: StandardSystem = StandardSystem("name")
        options: Options = Options()
        options.count = count

        # act
        results = model.go(options)

        # assert
        self.assertEqual(results.count, options.count)

# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()