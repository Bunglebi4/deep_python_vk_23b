import aiohttp
import asyncio
import unittest
from unittest.mock import patch
from acync_url_parser import fetch_url, main

class TestFetcher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.loop = asyncio.get_event_loop()

    def setUp(self):
        self.mock_session = None

    def tearDown(self):
        if self.mock_session:
            self.mock_session.__aexit__.assert_awaited()

    async def asyncSetUp(self):
        self.mock_session = self.get_mock_client_session()
        self.mock_session.__aenter__.return_value.get.return_value.__aenter__.\
            return_value.text.return_value\
            = 'Test Response'

    def get_mock_client_session(self):
        return self.patch('aiohttp.ClientSession')

    def patch(self, target):
        self.addCleanup(patch.stopall)
        return patch(target)

    async def test_fetch_url(self):
        url = 'http://example.com'
        response = await fetch_url(self.mock_session, url)
        self.assertEqual(response, 'Test Response')

    async def test_main(self):
        url_file = 'test_urls.txt'

        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = "http://example.com\nhttp://example.org\n"
            await main(2, url_file)

        self.assertEqual(self.mock_session.get.call_count, 2)

if __name__ == '__main__':
    unittest.main()