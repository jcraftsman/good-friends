from unittest import TestCase
from unittest.mock import Mock

# Think -> Red -> Green -> Refactor
#
# Guideline 1: Always start with outputs
# 
# Guideline 2: Behavior slicing
#
# Guideline 3: Simplify
#
class TestGoodFriends(TestCase):

    def setUp(self):
        pass

    def test_we_can_run_tests(self):
        # Assert
        self.assertEquals(1,1)
