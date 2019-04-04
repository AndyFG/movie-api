from test import BaseTest


class MainTest(BaseTest):
    endpoint = '/'

    def testMain(self):
        response = self.client().get(self.endpoint)

        self.assertEqual(response.status_code, 200)
