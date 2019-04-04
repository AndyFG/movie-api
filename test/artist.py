from test import BaseTest


class ArtistTest(BaseTest):
    endpoint = '/api/artist'
    headers = {'Content-Type': 'application/vnd.api+json'}

    def testList(self):
        response = self.client().get(self.endpoint, headers=self.headers)

        self.assertEqual(response.status_code, 200)
